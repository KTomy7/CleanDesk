import os
import json
import logging
from PyQt6.QtCore import QFile, QTextStream

def load_config(config_path="config.json"):
    """
    Loads the configuration from the 'config.json' file.
    """

    if not os.path.exists(config_path):
        logging.error(f"Configuration file '{config_path}' not found.")
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)

CONFIG = load_config()

# Set up logging globally
LOG_FILE = "cleandesk.log"
logging_level = getattr(logging, CONFIG.get("logging_level", "INFO").upper(), logging.INFO)
logging.basicConfig(
    level=logging_level,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler() 
    ]
)
    
def get_target_direcory():
    """
    Retrieves the target directory from the configuration file.
    """

    config = load_config()
    return config.get("target_directory")

def validate_directory(directory):
    """
    Checks if a directory exists. Returns True if valid, False otherwise.
    """

    if not os.path.isdir(directory):
        logging.error(f"The directory '{directory}' does not exist.")
        return False
    return True

def apply_stylesheet(app):
    file = QFile("resources/style.qss")
    if file.open(QFile.OpenModeFlag.ReadOnly):
        stream = QTextStream(file)
        qss = stream.readAll()
        app.setStyleSheet(qss)
        file.close()
        