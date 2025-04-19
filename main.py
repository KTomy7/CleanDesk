import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from helpers import apply_stylesheet, logger

if __name__ == "__main__":
    logger.info("CleanDesk started")
    app = QApplication(sys.argv)
    apply_stylesheet(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
