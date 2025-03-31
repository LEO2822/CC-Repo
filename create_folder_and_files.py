import os


def create_folder_and_files():
    # Get folder name from user
    folder_name = input("Enter the folder name: ")

    try:
        # Create the folder
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully!")

        # Create the three files
        files = ["code.py", "input.txt", "output.txt"]
        for file in files:
            file_path = os.path.join(folder_name, file)
            
            # Add the comment template to code.py
            if file == "code.py":
                with open(file_path, "w") as f:
                    f.write(f'"""\nhttps://www.codechef.com/problems/{folder_name}\n"""\n\n')
            else:
                with open(file_path, "w"):
                    pass
                    
            print(f"File '{file}' created successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    create_folder_and_files()
