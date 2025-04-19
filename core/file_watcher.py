import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.file_organizer import organize_files
from helpers import logger

class FileWatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"New file detected: {event.src_path}")
            try:
                organize_files(os.path.dirname(event.src_path))
                logger.info(f"Successfully organized file: {event.src_path}")
            except Exception as e:
                logger.error(f"Error while organizing file '{event.src_path}': {e}")
        else:
            logger.debug(f"Ignored directory creation event: {event.src_path}")

class FileMonitorThread(threading.Thread):
    def __init__(self, target_directory):
        super().__init__()
        self.target_directory = target_directory
        self._stop_event = threading.Event()

    def run(self):
        logger.info(f"Initializing file monitoring for directory: '{self.target_directory}'")
        event_handler = FileWatcherHandler()
        observer = Observer()
        observer.schedule(event_handler, path=self.target_directory, recursive=False)
        observer.start()

        logger.info(f"Monitoring started on '{self.target_directory}'...")

        try:
            while not self._stop_event.is_set():
                time.sleep(2)
        except Exception as e:
            logger.error(f"Error occurred in monitoring thread: {e}")
        finally:
            observer.stop()
            observer.join()
            logger.info("Monitoring stopped.")
    
    def stop(self):
        logger.info("Stopping file monitoring...")
        self._stop_event.set()
