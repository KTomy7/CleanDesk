from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from ui.file_browser import FileBrowser
from ui.settings import Settings
from core.file_organizer import organize_files
from core.file_watcher import FileMonitorThread
from helpers.utils import get_target_direcory, validate_directory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # Setup main window UI
        self.setWindowTitle("CleanDesk")
        self.setWindowIcon(QIcon("resources/icon.ico"))
        self.setGeometry(200, 200, 300, 250)

        # Create layout
        layout = QVBoxLayout()  # Use a local variable for the layout

        # Create file browser and settings widgets
        self.file_browser = FileBrowser(self)
        layout.addWidget(self.file_browser)

        self.settings = Settings(self)
        layout.addWidget(self.settings)

        # Add start/stop buttons for monitoring
        self.start_button = QPushButton("Start Monitoring")
        self.start_button.clicked.connect(self.start_monitoring)

        self.stop_button = QPushButton("Stop Monitoring")
        self.stop_button.clicked.connect(self.stop_monitoring)

        self.setButtonStates(True, False)
        
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        # Create a QWidget to hold the layout
        container = QWidget()
        container.setLayout(layout)  # Set the layout to the container widget
        self.setCentralWidget(container)

        self.monitor_thread = None  # Store the monitoring thread reference

    def setButtonStates(self, start_enabled, stop_enabled):
        self.start_button.setEnabled(start_enabled)
        self.stop_button.setEnabled(stop_enabled)

    def start_monitoring(self):
        self.setButtonStates(False, True)

        target_directory = get_target_direcory()
        if not validate_directory(target_directory):
            return  

        # Organize files in the target directory initially
        organize_files(target_directory)

        # Start the monitoring thread
        self.monitor_thread = FileMonitorThread(target_directory)
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.setButtonStates(True, False)

        if self.monitor_thread:
            self.monitor_thread.stop()
            self.monitor_thread = None
            print("Monitoring stopped.")
