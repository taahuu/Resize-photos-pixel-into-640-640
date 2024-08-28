import os

def delete_empty_files(folder_path):
    # Check if the provided folder path exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # Loop through all the files in the folder
    for filename in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)

        # Check if the path is a file and if it is empty (0 bytes)
        if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
            # Delete the file
            os.remove(file_path)
            print(f"Deleted empty file: {filename}")

    print("Operation completed.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    delete_empty_files(folder_path)
