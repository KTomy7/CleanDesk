import os
import shutil
import time
import logging
from utils import load_config   

CONFIG = load_config()

def organize_files(source_dir):
    """
    Scans and sorts files in the specified directory into categorized subfolders.
    """
    
    logging.info(f"Organizing files in '{source_dir}'...")

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            if is_old_file(file_path):
                move_file(file_path, os.path.join(source_dir, CONFIG["to_delete_files"]))
                continue
            
            ext = os.path.splitext(filename)[1].lower()
            destination_folder = None
                
            # Check if the file extension matches any category
            for folder, extensions in CONFIG["categories"].items():
                if ext in extensions:
                    destination_folder = os.path.join(source_dir, folder)
                    break

            # If no category matched, move the file to the 'Others' folder
            if destination_folder is None:
                destination_folder = os.path.join(source_dir, CONFIG["other_files"])

            move_file(file_path, destination_folder)        
                
def is_old_file(file_path):
    """
    Checks if the file was modified within the last 'days_to_consider' days.
    """

    if not os.path.exists(file_path):
        return False 

    file_modified_time = os.path.getmtime(file_path)  # Last modification time
    return (time.time() - file_modified_time) / (60 * 60 * 24) > CONFIG["days_to_consider"]

def move_file(file_path, destination_folder):
    """   
    Moves the specified file to the given destination folder, creating it if necessary.
    """
    
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
    logging.info(f"Moved '{os.path.basename(file_path)}' to '{os.path.basename(destination_folder)}'")