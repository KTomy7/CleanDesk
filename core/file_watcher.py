import os
import time
import logging
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.file_organizer import organize_files

class FileWatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            organize_files(os.path.dirname(event.src_path))

class FileMonitorThread(threading.Thread):
    def __init__(self, target_directory):
        super().__init__()
        self.target_directory = target_directory
        self._stop_event = threading.Event()

    def run(self):
        event_handler = FileWatcherHandler()
        observer = Observer()
        observer.schedule(event_handler, path=self.target_directory, recursive=False)
        observer.start()

        logging.info(f"Monitoring started on '{self.target_directory}'...")

        try:
            while not self._stop_event.is_set():
                time.sleep(2)
        finally:
            observer.stop()
            observer.join()
            logging.info("Monitoring stopped.")
    
    def stop(self):
        self._stop_event.set()
