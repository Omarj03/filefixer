import os
from os import path
from os import listdir
from shutil import move


# prompts user to press enter to continue
def to_continue():
    input("Press enter to continue...")
    print(f'\n' * 20)


# allows the user to enter a new working directory
def get_dir():
    while True:  # Input directory, check for validity and break if correct
        print("Enter folder directory:")
        new_user_dl_path = input("--> ")
        if path.isdir(new_user_dl_path):
            return new_user_dl_path
        else:
            print("Directory does not exist. Please Enter a valid directory")


# Sorts files by file type into folders.
def sort_files(user_dl_path, filemode="all", threshold=1):
    # Get list of items in directory
    dir_list = listdir(user_dl_path)

    # separate files
    files = [file for file in dir_list if path.isfile(user_dl_path + '\\' + file)]

    folders_made = 0
    files_moved = 0

    # sort all file types
    if filemode == "all":
        if threshold == 1:
            for file in files:
                # find last occurence of '.' in string and use to get extension
                ext_index = file.rfind('.')
                extension = "".join([char for char in file[ext_index::+1]])

                extension_directory = user_dl_path + '\\' + extension
                if not path.isdir(extension_directory):  # check if folder exists
                    os.makedirs(extension_directory)  # if it doesn't exist, make it
                    print(f"{extension} folder created")
                    folders_made += 1

                move(user_dl_path + "\\\\" + file, extension_directory)  # move file to appropriate folder
                files_moved = files_moved + 1

        else:
            ignored_filetypes = []
            iterator = -1
            while iterator < len(files):

                extension = "".join([char for char in (files[iterator])[files[iterator].rfind('.')::+1]])
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

                    else:
                        ignored_filetypes.append(extension)

                dir_list = listdir(user_dl_path)
                files = [file for file in dir_list if path.isfile(user_dl_path + '\\' + file)]
                iterator += 1

    else:
        filemode = '.' + filemode
        for file in files:
            # find last occurrence of '.' in string and use to get extension
            ext_index = file.rfind(".")
            extension = "".join([char for char in file[ext_index::+1]])

            if extension == filemode:  # check if file type is the same as inputted,
                extension_directory = user_dl_path + '\\' + extension
                if not path.isdir(extension_directory):  # if so, check if folder exists
                    os.makedirs(extension_directory)  # if it doesn't exist, make it
                    folders_made += 1
                move(user_dl_path + "\\\\" + file, extension_directory)  # move file to appropriate folder
                files_moved += 1
    print(f"Cleanup completed. Summary:\n\t{folders_made} folder(s) made. \n\t{files_moved} file(s) moved.")
    to_continue()
