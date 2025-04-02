from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QFileDialog
from helpers.utils import get_target_direcory, validate_directory

class FileBrowser(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the initial directory path
        directory_path = get_target_direcory()

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

    def set_label_text(self, directoryPath):
        self.label.setText(f"Selected folder: {directoryPath}")  

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Downloads Folder")
        if directory:
            self.set_label_text(directory)
            # You can save this path for use in your app, e.g., save it to a config or variable
