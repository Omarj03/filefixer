import os
import re
from os import path
from os import listdir
from re import finditer
from shutil import move

import functions as f


# Menu
def cli(user_dl_path):
    option = 0

    while True:
        print(f'\n' * 20)
        print(f'''FileFixer Build 04/03/2023
Current Directory: {user_dl_path}
--------------------------
Please select an option below:
    1. Sort files by file type
    2. Remove duplicates
    3. Sort files by file type & remove duplicates
    4. Change directory
    5. Exit
--> ''', end='')
        try:
            option = input()

            match option:
                case '1':
                    sort_files(user_dl_path)
                case '2':
                    remove_duplicates()
                case '3':
                    remove_duplicates()
                    sort_files()
                case '4':
                    user_dl_path = get_dir(user_dl_path)
                case '5':
                    break
                case other:
                    print("Invalid input. Please select option 1,2,3,4, or 5.")
                    f.to_continue()
        except Exception as e:
            print(f"\nError {e}:  Please try again or exit application.")
            f.to_continue()


### Menu Options ###


# allows the user to enter a new working directory
def get_dir(user_dl_path):
    while True:  # Input directory, check for validity and break if correct
        print("Enter folder directory:")
        new_user_dl_path = input("--> ")
        if path.isdir(new_user_dl_path):
            return new_user_dl_path
            break
        else:
            print("Directory does not exist. Please Enter a valid directory")





# Removes duplicate files in a directory
def remove_duplicates():
    f.to_continue()


# Sorts files by file type into folders.
def sort_files(user_dl_path):
    # Get list of items in directory
    dir_list = listdir(user_dl_path)

    # seperate files and folders
    files = [file for file in dir_list if path.isfile(user_dl_path+'\\'+file)]
    folders = [folder for folder in dir_list if path.isdir(user_dl_path+ '\\'+folder)]


    for file in files:
        ## find last occurence of '.' in string and use to get extension
        ext_index = file.rfind(".")

        extension = "".join([char for char in file[ext_index::+1]])

        extension_directory = user_dl_path+'\\'+extension
        folders_made = 0
        files_moved = 0

        if not path.isdir(extension_directory):
            os.makedirs(extension_directory)
            folders_made += 1

        move(user_dl_path+"\\\\"+file, extension_directory)
        files_moved = files_moved + 1
    print(f"Cleanup completed. Summary:\n\t{folders_made} folder(s) made. \n\t{files_moved} file(s) moved.")
    f.to_continue()


### main ###

def main():
    user_home_path = path.expanduser('~')
    user_dl_path = path.join(user_home_path, "Downloads")

    cli(user_dl_path)


if __name__ == "__main__":
    main()
