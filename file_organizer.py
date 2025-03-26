import os
import shutil

# Define your folder categories
CATEGORY_MAP = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    "Music": [".mp3", ".wav", ".flac"],
    "Executables": [".exe", ".msi"],
}

def organize_files(source_dir):
    """
    Scans and sorts files in the specified directory into categorized subfolders.
    """

    if not os.path.isdir(source_dir):
        print(f"Error: The directory '{source_dir}' does not exist.")
        return

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            destination_folder = None
            
            # Check if the file extension matches any category
            for folder, extensions in CATEGORY_MAP.items():
                if ext in extensions:
                    destination_folder = os.path.join(source_dir, folder)
                    break

            # If no category matched, move the file to the 'Others' folder
            if destination_folder is None:
                destination_folder = os.path.join(source_dir, "Others")

            move_file(file_path, destination_folder)    
            

def move_file(file_path, destination_folder):
    """   
    Moves the specified file to the given destination folder, creating it if necessary.
    """

    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
    print(f"Moved '{os.path.basename(file_path)}' to '{os.path.basename(destination_folder)}'")