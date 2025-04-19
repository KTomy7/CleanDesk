import os
from PyQt6.QtCore import QFile, QTextStream
from helpers.logger import logger
from helpers.config_helper import get_config_value
    
def get_target_directory():
    """
    Retrieves the target directory from the configuration file.
    """
    logger.info("Retrieving target directory from configuration.")
    directory = get_config_value("target_directory")

    if validate_directory(directory):
        logger.info(f"Target directory returned: '{directory}'.")
        return directory
    else:
        logger.error(f"Invalid target directory: {directory}")
        raise ValueError(f"Invalid target directory: {directory}")

def validate_directory(directory):
    """
    Checks if a directory exists. Returns True if valid, False otherwise.
    """
    logger.info(f"Validating directory: '{directory}'.")
    if os.path.isdir(directory):
        logger.info(f"Directory '{directory}' exists and is valid.")
        return True
    else:
        logger.warning(f"Directory '{directory}' does not exist or is invalid.")
        return False

def apply_stylesheet(app):
    """
    Applies a stylesheet to the given PyQt application.
    """
    logger.info("Attempting to apply stylesheet from 'resources/style.qss'.")
    file = QFile("resources/style.qss")
    if file.open(QFile.OpenModeFlag.ReadOnly):
        try:
            stream = QTextStream(file)
            qss = stream.readAll()
            app.setStyleSheet(qss)
            logger.info("Stylesheet successfully applied.")
        except Exception as e:
            logger.error(f"Error applying stylesheet: {e}")
        finally:
            file.close()
    else:
        logger.error("Failed to open 'resources/style.qss'.")
        