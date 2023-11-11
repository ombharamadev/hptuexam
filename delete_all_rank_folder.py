import os
import shutil

def delete_all_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            try:
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                print(f"Error deleting folder {folder_path}: {e}")

# Replace 'path/to/your/directory' with the path of the directory containing the folders you want to delete
directory_path = 'rank'
delete_all_folders(directory_path)
