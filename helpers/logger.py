import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, base_filename, when, interval, backupCount, encoding=None, delay=False):
        
        logs_directory = "logs"
        if not os.path.exists(logs_directory):
            os.makedirs(logs_directory)

        current_date = datetime.now().strftime("%d-%m-%Y")
        log_filename = os.path.join(logs_directory, f"CleanDesk-log_{current_date}.log")

        # Initialize the TimedRotatingFileHandler with the custom log filename
        super().__init__(log_filename, when=when, interval=interval, backupCount=backupCount, encoding=encoding, delay=delay)

    def doRollover(self):
        """
        Perform the rollover to a new log file. This method will be called automatically by the handler.
        We override this to customize the log filename with the current date.
        """
        
        current_date = datetime.now().strftime("%Y-%m-%d")
        log_filename = os.path.join("logs", f"CleanDesk-log_{current_date}.log")

        # Perform the rollover
        self.stream.close()
        self.rotate(self.baseFilename, log_filename)
        self.stream = self._open()

def setup_logger():
    # Set up logger
    logger = logging.getLogger("CleanDeskApp")
    logger.setLevel(logging.INFO)  # Set the global logging level

    # Set up the custom handler with daily log rotation
    log_handler = CustomTimedRotatingFileHandler(
        "app_log",  # Base filename without the date
        when="midnight",  # Rotate at midnight every day
        interval=1,  # Rotate every day
        backupCount=7,  # Keep the last 7 days of logs
        encoding="utf-8"  # Optional encoding
    )

    # Set the formatter for the log handler
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_formatter)

    # Add the handler to the logger
    logger.addHandler(log_handler)

    return logger

logger = setup_logger()
