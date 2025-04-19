from PyQt6.QtWidgets import QWidget, QLabel, QSpinBox, QHBoxLayout, QVBoxLayout, QCheckBox
from helpers import logger, get_config_value, update_config_value

class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        logger.info("Initializing Settings widget.")

        # Create threshold input label and spin box
        self.label = QLabel("Set threshold for moving old files (in days):")
        self.threshold_input = QSpinBox()
        self.threshold_input.setRange(1, 365)
        self.threshold_input.setValue(get_config_value("days_to_consider")) 
        self.threshold_input.setFixedWidth(50)
        self.threshold_input.valueChanged.connect(self.on_threshold_changed)
        logger.info(f"Threshold input spin box created with initial value: {get_config_value('days_to_consider')}.")

        threshold_layout = QHBoxLayout()
        threshold_layout.addWidget(self.label)
        threshold_layout.addWidget(self.threshold_input)

        # Create the checkbox
        self.auto_delete_checkbox = QCheckBox("Automatically delete old files")
        self.auto_delete_checkbox.setChecked(get_config_value("auto_delete_old_files"))
        self.auto_delete_checkbox.stateChanged.connect(self.on_auto_delete_changed)

        checkbox_layout = QVBoxLayout()
        checkbox_layout.addWidget(self.auto_delete_checkbox)

        # Create layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(threshold_layout)
        main_layout.addLayout(checkbox_layout)
        self.setLayout(main_layout)
        logger.info("Settings widget layout set up.")

    def on_threshold_changed(self, value):
        """
        Called when the threshold value is changed in the UI.
        """
        update_config_value("days_to_consider", value)
        logger.info(f"Threshold changed to: {value} days.")

    def on_auto_delete_changed(self, state):
        """
        Called when the auto-delete checkbox is checked or unchecked.
        """
        is_checked = state == 2  # PyQt6 uses 2 for checked, 0 for unchecked
        update_config_value("auto_delete_old_files", is_checked)
        logger.info(f"Auto-delete checkbox state changed to: {'Checked' if is_checked else 'Unchecked'}.")
