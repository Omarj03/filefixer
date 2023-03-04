from os import path
from os import listdir


### Functions ###

# prompts user to press enter to continue
def to_continue():
    input("Press enter to continue...")
    print(f'\n' * 20)

# Sorts files by file type into folders.
def sort_files(user_dl_path):
    dir_list = listdir(user_dl_path)
    print(dir_list)

    to_continue()

# Removes duplicate files in a directory
def remove_duplicates():
    to_continue()


# Interface
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
            option = int(input())

            match option:
                case 1:
                    sort_files(user_dl_path)
                case 2:
                    remove_duplicates()
                case 3:
                    remove_duplicates()
                    sort_files()
                case 4:
                    get_dir(user_dl_path)
                case 5:
                    break
                case other:
                    print("Invalid input. Please select option 1,2,3, or 4.")
                    to_continue()
        except:
            print("\nInvalid input. Please select option 1,2,3, or 4.")
            to_continue()


def get_dir(user_dl_path):


    while True:  # Input directory, check for validity and break if correct
        print("Enter folder directory:")
        user_dl_path = input("--> ")
        if path.isdir(user_dl_path):
            break
        else:
            print("Directory does not exist. Please Enter a valid directory")
            


### main ###
def main():
    user_home_path = path.expanduser('~')
    user_dl_path = path.join(user_home_path, "Downloads")

    cli(user_dl_path)


if __name__ == "__main__":
    main()
