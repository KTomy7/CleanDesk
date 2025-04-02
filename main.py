import sys
import logging
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from helpers.utils import apply_stylesheet

if __name__ == "__main__":
    logging.info("CleanDesk started")
    app = QApplication(sys.argv)
    apply_stylesheet(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
