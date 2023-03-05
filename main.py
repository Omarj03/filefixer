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
    1. Sort one filetype
    2. sort all files over threshold
    3. sort all files
    4. Change directory
    5. Exit
--> ''', end='')
        try:
            option = input()

            match option:
                case '1':
                    while True:
                        filetype = input("Enter filetype --> .").lower()
                        if '.' in filetype:
                            print("Invalid input. Please enter filetype, ommitting the '.'.")
                        else:
                            sort_files(user_dl_path,filetype)
                            break

                case '2':
                    while True:
                        try:
                            threshold = int(input("Enter threshold for file type --> "))
                            if threshold == 0:
                                raise ValueError()
                            break
                        except:
                            print("Please enter a number (integer) greater than 0.")
                            f.to_continue()
                    sort_files(user_dl_path,"all",threshold)
                case '3':
                    sort_files(user_dl_path)
                case '4':
                   user_dl_path = get_dir(user_dl_path)
                case '5':
                    break
                case other:
                    print("Invalid input. Please select option 1,2,3,4, or 5.")
                    f.to_continue()
        except Exception as e:
            print(f"\nError: {e},  Please try again or exit application.")
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





# Sorts files by file type into folders.
def sort_files(user_dl_path, filemode="all",threshold = 1):
    # Get list of items in directory
    dir_list = listdir(user_dl_path)

    # seperate files
    files = [file for file in dir_list if path.isfile(user_dl_path+'\\'+file)]

    folders_made = 0
    files_moved = 0

    # sort all file types
    if filemode == "all":
        if threshold == 1:
            for file in files:
                ## find last occurence of '.' in string and use to get extension
                ext_index = file.rfind('.')
                extension = "".join([char for char in file[ext_index::+1]])

                extension_directory = user_dl_path + '\\' + extension
                if not path.isdir(extension_directory): # check if folder exists
                    os.makedirs(extension_directory) # if it doesn't exist, make it
                    folders_made += 1

                move(user_dl_path+"\\\\"+file, extension_directory)  # move file to appropriate folder
                files_moved = files_moved + 1

        else:
            ignored_filetypes = []
            iterator = 0
            while iterator <= len(files)+1:

                file = files[iterator]

                extension = "".join([char for char in (files[0])[files[0].rfind('.')::+1]])
                if extension not in ignored_filetypes:
                    ext_list = [file for file in files if extension in file]

                    extension_directory = user_dl_path + '\\' + extension
                    if len(ext_list) >= threshold:
                        if not path.isdir(extension_directory):  # check if folder exists
                            os.makedirs(extension_directory)  # if it doesn't exist, make it
                            folders_made += 1

                        for file in ext_list:
                            move(user_dl_path + "\\\\" + file, extension_directory)  # move file to appropriate folder
                            files_moved = files_moved + 1
                            files = [file for file in dir_list if path.isfile(user_dl_path + '\\' + file)]
                            iterator +=1

                    else:
                        ignored_filetypes.append(extension)
                    print(ext_list)
                    print(files)


    else:
        filemode = '.' + filemode
        for file in files:
            # find last occurence of '.' in string and use to get extension
            ext_index = file.rfind(".")
            extension = "".join([char for char in file[ext_index::+1]])


            if extension == filemode:         # check if file type is the same as inputted,
                extension_directory = user_dl_path + '\\' + extension
                if not path.isdir(extension_directory):            # if so, check if folder exists
                    os.makedirs(extension_directory)            # if it doesn't exist, make it
                    folders_made += 1
                move(user_dl_path+"\\\\"+file, extension_directory)            # move file to appropriate folder
                files_moved += 1
    print(f"Cleanup completed. Summary:\n\t{folders_made} folder(s) made. \n\t{files_moved} file(s) moved.")
    f.to_continue()


### main ###

def main():
    user_home_path = path.expanduser('~')
    user_dl_path = path.join(user_home_path, "Downloads")

    cli(user_dl_path)


if __name__ == "__main__":
    main()
