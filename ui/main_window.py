from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from ui.file_browser import FileBrowser
from ui.settings import Settings
from core.file_organizer import organize_files
from core.file_watcher import FileMonitorThread
from helpers import get_target_directory, logger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # Setup main window UI
        self.setWindowTitle("CleanDesk")
        self.setWindowIcon(QIcon("resources/icon.ico"))
        self.setGeometry(200, 200, 300, 250)
        logger.info("Main window initialized.")
        
        # Create layout
        layout = QVBoxLayout()  # Use a local variable for the layout

        # Create file browser and settings widgets
        self.file_browser = FileBrowser(self)
        layout.addWidget(self.file_browser)
        logger.info("FileBrowser widget added to the main window.")

        self.settings = Settings(self)
        layout.addWidget(self.settings)
        logger.info("Settings widget added to the main window.")

        # Add start/stop buttons for monitoring
        self.start_button = QPushButton("Start Monitoring")
        self.start_button.clicked.connect(self.start_monitoring)
        logger.info("Start Monitoring button created and connected.")

        self.stop_button = QPushButton("Stop Monitoring")
        self.stop_button.clicked.connect(self.stop_monitoring)
        logger.info("Stop Monitoring button created and connected.")

        self.setButtonStates(True, False)
        logger.info("Initial button states set: Start enabled, Stop disabled.")
        
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        # Create a QWidget to hold the layout
        container = QWidget()
        container.setLayout(layout)  # Set the layout to the container widget
        self.setCentralWidget(container)
        logger.info("Main window layout and widgets set up.")

        self.monitor_thread = None  # Store the monitoring thread reference

    def setButtonStates(self, start_enabled, stop_enabled):
        logger.info(f"Setting button states: Start enabled={start_enabled}, Stop enabled={stop_enabled}.")
        self.start_button.setEnabled(start_enabled)
        self.stop_button.setEnabled(stop_enabled)

    def start_monitoring(self):
        logger.info("Start Monitoring button clicked.")
        self.setButtonStates(False, True)

        try:
            target_directory = get_target_directory()
            logger.info(f"Target directory retrieved: '{target_directory}'.")

            # Organize files in the target directory initially
            logger.info("Organizing files in the target directory before starting monitoring.")
            organize_files(target_directory)

            # Start the monitoring thread
            self.monitor_thread = FileMonitorThread(target_directory)
            self.monitor_thread.start()
            logger.info("File monitoring thread started.")
        except Exception as e:
            logger.error(f"Error while starting monitoring: {e}")
            self.setButtonStates(True, False)

    def stop_monitoring(self):
        logger.info("Stop Monitoring button clicked.")
        self.setButtonStates(True, False)

        if self.monitor_thread:
            logger.info("Stopping the file monitoring thread.")
            self.monitor_thread.stop()
            self.monitor_thread = None
            logger.info("File monitoring thread stopped.")
        else:
            logger.warning("Stop Monitoring button clicked, but no monitoring thread was active.")
