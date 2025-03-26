from file_organizer import organize_files
from watcher import start_monitoring
from utils import get_target_direcory, validate_directory

if __name__ == "__main__":
    path = get_target_direcory() # Get the target directory from the configuration file
    if not validate_directory(path):
        exit(1)

    organize_files(path) # Organize files
    start_monitoring(path) # Start monitoring for new files
