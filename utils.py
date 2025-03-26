import os
import json

def load_config(config_path="config.json"):
    """
    Loads the configuration from the 'config.json' file.
    """

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
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
        print(f"Error: The directory '{directory}' does not exist.")
        return False
    return True