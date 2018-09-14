import os
from textwrap import dedent

def images_options(df_val, args):
    '''
    Manage the options for the images downloader.

    :param df_val: DataFrame Value.
    :param args: argument parser.
    :return: modified df_val
    '''
    if args.image_IsOccluded is not None:
        rejectedID = df_val.ImageID[df_val.IsOccluded != int(args.image_IsOccluded)].values
        df_val = df_val[~df_val.ImageID.isin(rejectedID)]

    if args.image_IsTruncated is not None:
        rejectedID = df_val.ImageID[df_val.IsTruncated != int(args.image_IsTruncated)].values
        df_val = df_val[~df_val.ImageID.isin(rejectedID)]

    if args.image_IsGroupOf is not None:
        rejectedID = df_val.ImageID[df_val.IsGroupOf != int(args.image_IsGroupOf)].values
        df_val = df_val[~df_val.ImageID.isin(rejectedID)]

    if args.image_IsDepiction is not None:
        rejectedID = df_val.ImageID[df_val.IsDepiction != int(args.image_IsDepiction)].values
        df_val = df_val[~df_val.ImageID.isin(rejectedID)]

    if args.image_IsInside is not None:
        rejectedID = df_val.ImageID[df_val.IsInside != int(args.image_IsInside)].values
        df_val = df_val[~df_val.ImageID.isin(rejectedID)]

    return df_val

def mkdirs(Dataset_folder, csv_folder, classes, type_csv):
    '''
    Make the folder structure for the system.

    :param Dataset_folder: Self explanatory
    :param csv_folder: folder path of csv files
    :param classes: list of classes to download
    :param type_csv: train, validation, test or all 
    :return: None
    '''

    directory_list = ['train', 'validation', 'test']
    
    if not type_csv == 'all':
        for class_name in classes:
            folder = os.path.join(Dataset_folder, type_csv, class_name, 'Label')
            if not os.path.exists(folder):
                os.makedirs(folder)
            filelist = [f for f in os.listdir(folder) if f.endswith(".txt")]
            for f in filelist:
                os.remove(os.path.join(folder, f))

    else:
        for directory in directory_list:
            for class_name in classes:
                folder = os.path.join(Dataset_folder, directory, class_name, 'Label')
                if not os.path.exists(folder):
                    os.makedirs(folder)
                filelist = [f for f in os.listdir(folder) if f.endswith(".txt")]
                for f in filelist:
                    os.remove(os.path.join(folder, f))

def progression_bar(total_images, index):
    '''
    Print the progression bar for the download of the images.

    :param total_images: self explanatory
    :param index: self explanatory
    :return: None
    '''
    rows, columns = os.popen('stty size', 'r').read().split()
    toolbar_width = int(columns) - 10
    image_index = index
    index = int(index / total_images * toolbar_width)

    print(' ' * (toolbar_width), end='\r')
    bar = "[{}{}] {}/{}".format('-' * index, ' ' * (toolbar_width - index), image_index, total_images)
    print(bar.rjust(int(columns)), end='\r')

def show_classes(classes):
    '''imag
    Show the downloaded classes in the selected folder during visualization mode
    '''
    for n in classes:
        print("- {}".format(n))
    print("\n")

def logo(command):
    '''
    Print the logo for the downloader and the visualizer when selected
    '''
    print("""
		   ___   _____  ______            _    _    
		 .'   `.|_   _||_   _ `.         | |  | |   
		/  .-.  \ | |    | | `. \ _   __ | |__| |_  
		| |   | | | |    | |  | |[ \ [  ]|____   _| 
		\  `-'  /_| |_  _| |_.' / \ \/ /     _| |_  
		 `.___.'|_____||______.'   \__/     |_____|
	""")

    if command == 'download':
        print('''
             _____                    _                 _             
            (____ \                  | |               | |            
             _   \ \ ___  _ _ _ ____ | | ___   ____  _ | | ____  ____ 
            | |   | / _ \| | | |  _ \| |/ _ \ / _  |/ || |/ _  )/ ___)
            | |__/ / |_| | | | | | | | | |_| ( ( | ( (_| ( (/ /| |    
            |_____/ \___/ \____|_| |_|_|\___/ \_||_|\____|\____)_|    
                                                          
        ''')

    if command == 'visualize':
        print(""" 
                 _    _ _                  _ _                  
                | |  | (_)                | (_)                 
                | |  | |_  ___ _   _  ____| |_ _____ ____  ____ 
                 \ \/ /| |/___) | | |/ _  | | (___  ) _  )/ ___)
                  \  / | |___ | |_| ( ( | | | |/ __( (/ /| |    
                   \/  |_(___/ \____|\_||_|_|_(_____)____)_|    
                                                                                                                                                                                                    
""")

