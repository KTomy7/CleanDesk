import json
import os
from helpers import logger

CONFIG_FILE_PATH = 'config.json'
DEFAULT_CONFIG = {
    "target_directory": "path/to/your/Downloads",
    "logging_level": "INFO",
    "categories": {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".tar", ".gz", ".rar"],
        "Executables": [".exe", ".msi"]
    },
    "other_files": "Others",
    "auto_delete": False, 
    "threshold_days": 30 
}

def load_config():
    """
    Load configuration from the config file or use default values.
    """
    logger.info(f"Attempting to load configuration from '{CONFIG_FILE_PATH}'.")
    if not os.path.exists(CONFIG_FILE_PATH):
        logger.error(f"Configuration file '{CONFIG_FILE_PATH}' not found. Creating a new one with default values.")
        save_config(DEFAULT_CONFIG)

    try:
        with open(CONFIG_FILE_PATH, 'r', encoding="utf-8") as config_file:
            config = json.load(config_file)
            logger.info(f"Configuration successfully loaded from '{config_file}'.")
            return config
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from '{CONFIG_FILE_PATH}': {e}")
        raise

def save_config(config_data):
    """
    Save the configuration to the config file.
    """
    logger.info(f"Saving configuration to '{CONFIG_FILE_PATH}'.")
    try:
        with open(CONFIG_FILE_PATH, 'w', encoding="utf-8") as config_file:
            json.dump(config_data, config_file, indent=4)
            logger.info(f"Configuration successfully saved to '{CONFIG_FILE_PATH}'.")
    except IOError as e:
        logger.error(f"Error writing to configuration file '{CONFIG_FILE_PATH}': {e}")
        raise

def get_config_value(key):
    """
    Get a specific configuration value by key.
    """
    logger.info(f"Retrieving configuration value for key: '{key}'.")
    config = load_config()
    return config.get(key)

# Update a specific configuration value and save the config
def update_config_value(key, value):
    """
    Update a specific configuration value and save the config.
    """
    logger.info(f"Updating configuration value for key: '{key}' to '{value}'.")
    config = load_config()
    config[key] = value
    save_config(config)
