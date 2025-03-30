    
import time
import os
import logging
import threading
import keyboard
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.file_organizer import organize_files

running = True

def stop_program():
    global running
    keyboard.wait("ctrl+c")  # Wait until Ctrl + C is pressed
    logging.info("Ctrl + C detected! Stopping the program...")
    running = False 

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
    
    stop_thread = threading.Thread(target=stop_program, daemon=True)
    stop_thread.start()
    
    logging.info(f"Monitoring started on '{target_directory}'... Press Ctrl+C to stop.")

    try:
        while running:
            time.sleep(2)
    finally:
        observer.stop()
        observer.join()

        logging.info("Monitoring stopped.")
        logging.info("CleanDesk stopped.")
