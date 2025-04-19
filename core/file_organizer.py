import os
import shutil
import time
from helpers import load_config, logger   

CONFIG = load_config()

def organize_files(source_dir):
    """
    Scans and sorts files in the specified directory into categorized subfolders.
    """
    
    logger.info(f"Starting to organize files in '{source_dir}'...")

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            logger.debug(f"Processing file: '{filename}'")
            if is_old_file(file_path):
                logger.info(f"File '{filename}' is considered old. Moving to '{CONFIG['to_delete_files']}' folder.")
                move_file(file_path, os.path.join(source_dir, CONFIG["to_delete_files"]))
                continue
            
            ext = os.path.splitext(filename)[1].lower()
            destination_folder = None
                
            # Check if the file extension matches any category
            for folder, extensions in CONFIG["categories"].items():
                if ext in extensions:
                    destination_folder = os.path.join(source_dir, folder)
                    logger.debug(f"File '{filename}' matches category '{folder}' based on extension '{ext}'.")
                    break

            # If no category matched, move the file to the 'Others' folder
            if destination_folder is None:
                destination_folder = os.path.join(source_dir, CONFIG["other_files"])
                logger.debug(f"File '{filename}' does not match any category. Moving to 'Others' folder.")

            move_file(file_path, destination_folder)        
        else:
            logger.debug(f"Skipping non-file item: '{filename}'")
    
    logger.info(f"Finished organizing files in '{source_dir}'.")
                
def is_old_file(file_path):
    """
    Checks if the file was modified within the last 'days_to_consider' days.
    """

    if not os.path.exists(file_path):
        logger.error(f"File path does not exist: '{file_path}'")
        return False 

    file_modified_time = os.path.getmtime(file_path)  # Last modification time
    is_old = (time.time() - file_modified_time) / (60 * 60 * 24) > CONFIG["days_to_consider"]
    logger.debug(f"File '{os.path.basename(file_path)}' is {'old' if is_old else 'not old'} based on modification time.")
    return is_old

def move_file(file_path, destination_folder):
    """   
    Moves the specified file to the given destination folder, creating it if necessary.
    """
    
    try:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
        logger.info(f"Moved '{os.path.basename(file_path)}' to '{destination_folder}'.")
    except Exception as e:
        logger.error(f"Failed to move file '{file_path}' to '{destination_folder}': {e}")
        