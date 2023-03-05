from os import path
import control as c


# Menu
def cli(user_dl_path):
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
                            c.sort_files(user_dl_path, filetype)
                            break

                case '2':
                    while True:
                        try:
                            threshold = int(input("Enter threshold for file type --> "))
                            if threshold == 0:
                                raise ValueError()
                            break
                        except ValueError as e:
                            print(f"Error: {e},Please enter a number (integer) greater than 0.")
                            c.to_continue()
                    c.sort_files(user_dl_path, "all", threshold)
                case '3':
                    c.sort_files(user_dl_path)
                case '4':
                    user_dl_path = c.get_dir()
                case '5':
                    break
                case _:
                    print("Invalid input. Please select option 1,2,3,4, or 5.")
                    c.to_continue()
        except Exception as e:
            print(f"\nError: {e},  Please try again or exit application.")
            c.to_continue()


def main():
    user_home_path = path.expanduser('~')
    user_dl_path = path.join(user_home_path, "Downloads")

    cli(user_dl_path)


if __name__ == "__main__":
    main()
