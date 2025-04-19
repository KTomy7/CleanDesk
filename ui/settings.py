from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QHBoxLayout
from helpers import load_config, logger

CONFIG = load_config()
class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        logger.info("Initializing Settings widget.")

        self.label = QLabel("Set threshold for moving old files (in days):")
        self.threshold_input = QSpinBox()
        self.threshold_input.setRange(1, 365)
        self.threshold_input.setValue(CONFIG["days_to_consider"]) 
        self.threshold_input.setFixedWidth(50)
        logger.debug(f"Threshold input spin box created with initial value: {CONFIG['days_to_consider']}.")

        # Create layout
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.threshold_input)
        self.setLayout(layout)
        logger.info("Settings widget layout set up.")

    def get_threshold(self):
        threshold = self.threshold_input.value()
        logger.debug(f"Threshold value retrieved: {threshold}.")
        return threshold
