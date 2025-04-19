from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QFileDialog
from helpers import get_target_directory, logger

class FileBrowser(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the initial directory path
        try:
            directory_path = get_target_directory()
            logger.info(f"Initial directory path retrieved: '{directory_path}'")
        except Exception as e:
            logger.error(f"Failed to retrieve initial directory path: {e}")
            directory_path = ""

        # Create the label and browse button    
        self.label = QLabel()
        self.set_label_text(directory_path)
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_directory)

        # Create layout 
        layout = QHBoxLayout() 
        layout.addWidget(self.label)
        layout.addWidget(self.browse_button)

        self.setLayout(layout)
        logger.info("FileBrowser UI initialized.")

    def set_label_text(self, directoryPath):
        logger.info(f"Setting label text to: 'Selected folder: {directoryPath}'")
        self.label.setText(f"Selected folder: {directoryPath}")  

    def browse_directory(self):
        logger.info("Opening directory selection dialog.")
        directory = QFileDialog.getExistingDirectory(self, "Select Downloads Folder")
        if directory:
            logger.info(f"Directory selected: '{directory}'")
            self.set_label_text(directory)
            # You can save this path for use in your app, e.g., save it to a config or variable
        else:
            logger.warning("No directory selected.")
