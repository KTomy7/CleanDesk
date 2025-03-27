    
import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from file_organizer import organize_files

class CleanDeskHandler(FileSystemEventHandler):
    # Event handler for the watchdog observer
    # This class will be used to handle the events triggered by the observer
    def on_created(self, event):
        # Check if the event is not a directory
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            organize_files(os.path.dirname(event.src_path))

def start_monitoring(target_directory):
    """
    Starts monitoring the specified directory for new files.
    """
    
    event_handler = CleanDeskHandler()
    observer = Observer()
    observer.schedule(event_handler, path=target_directory, recursive=False)
    observer.start()

    print(f"Monitoring started on '{target_directory}'... Press Ctrl+C to stop.")
    logging.info(f"Monitoring started on '{target_directory}'...")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopping monitoring...")
        logging.info("\nStopping monitoring...")
        
        observer.stop()
        observer.join()
        
        print("Monitoring stopped.")
        logging.info("Monitoring stopped.")
        logging.info("CleanDesk stopped.")
