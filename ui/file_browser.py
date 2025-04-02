from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QFileDialog

class FileBrowser(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the label and browse button
        self.label = QLabel("Selected folder:")
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_directory)

        # Create layout 
        layout = QHBoxLayout() 
        layout.addWidget(self.label)
        layout.addWidget(self.browse_button)

        self.setLayout(layout)       

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Downloads Folder")
        if directory:
            self.label.setText(f"Selected folder: {directory}")
            # You can save this path for use in your app, e.g., save it to a config or variable
            print(f"Selected directory: {directory}")
