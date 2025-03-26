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

    # Check if the source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a valid directory path")
        return

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            # Check if the file extension matches any category
            for folder, extensions in CATEGORY_MAP.items():
                if ext in extensions:
                    destination_folder = os.path.join(source_dir, folder)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"Moved '{filename}' to '{folder}/'")
                    moved = True
                    break

            if not moved:
                destination_folder = os.path.join(source_dir, 'Others')
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved '{filename}' to 'Others/'")