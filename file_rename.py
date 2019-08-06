"""
Rename files from a folder
get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""

import os




def rename_files():
    """
    Rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\cooperrictor.AD\Desktop\Hafb\prankorig"
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()                #saves current working directory
    #change directory to the files directory so that you can change the file names
    os.chdir(folder_dir)
    for file in files:
        #remove digits from name
        new_file = file.lstrip('0123456789')
        print("Old name", file, "New name", new_file)
        #rename file to new name
        os.renames(file, new_file)
    #get back to home directory
    os.chdir(saved_path)


def main():
    """
    test function
    :return: nothing
    """
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)