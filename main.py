import control as c


# Menu
def cli(working_dir):
    while True:
        print(f'\n' * 20)
        print(f'''FileFixer Build 05/03/2023
Current Directory: {working_dir}
--------------------------
Please select an option below:
    1. Sort one filetype
    2. Sort all files over threshold
    3. Sort all files
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
                            c.sort_files(working_dir, filetype)
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
                    c.sort_files(working_dir, "all", threshold)
                case '3':
                    c.sort_files(working_dir)
                case '4':
                    working_dir = c.get_dir()
                case '5':
                    break
                case _:
                    print("Invalid input. Please select option 1,2,3,4, or 5.")
                    c.to_continue()
        except Exception as e:
            print(f"\nError: {e},  Please try again or exit application.")
            c.to_continue()

# Main startup
def main():
    working_dir = c.get_dir()
    cli(working_dir)


if __name__ == "__main__":
    main()
