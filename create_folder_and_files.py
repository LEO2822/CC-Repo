import os


def create_folder_and_files():
    # Get details from user
    folder_name = input("Enter the folder name: ")
    provider = input("Enter the provider (codeforces, codechef, leetcode, etc.): ")
    problem_link = input("Enter the problem statement link: ")

    try:
        # Create the folder
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully!")

        # Create the three files
        files = ["code.py", "input.txt", "output.txt"]
        for file in files:
            file_path = os.path.join(folder_name, file)

            # Add the comment template + I/O boilerplate to code.py
            if file == "code.py":
                template = (
                    f'"""\n{provider}\n{problem_link}\n"""\n\n'
                    "import sys\n"
                    "import os\n\n"
                    "script_dir = os.path.dirname(os.path.abspath(__file__))\n\n"
                    'sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")\n'
                    'sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")\n\n'
                )
                with open(file_path, "w") as f:
                    f.write(template)
            else:
                with open(file_path, "w"):
                    pass

            print(f"File '{file}' created successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    create_folder_and_files()
