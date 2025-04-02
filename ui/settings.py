from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QHBoxLayout
from utils import load_config

CONFIG = load_config()
class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel("Set threshold for moving old files (in days):")
        self.threshold_input = QSpinBox()
        self.threshold_input.setRange(1, 365)
        self.threshold_input.setValue(CONFIG["days_to_consider"]) 
        self.threshold_input.setFixedWidth(50)

        # Create layout
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.threshold_input)

        self.setLayout(layout)

    def get_threshold(self):
        return self.threshold_input.value()
    
    
