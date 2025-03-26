from file_organizer import organize_files
from watcher import start_monitoring

if __name__ == "__main__":
    path = "C:/Users/kisst/Downloads"  
    organize_files(path) # Organize files
    start_monitoring(path) # Start monitoring for new files
