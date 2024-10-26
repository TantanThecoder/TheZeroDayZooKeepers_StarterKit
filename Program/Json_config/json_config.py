import logging
import json
from pathlib import Path

class Json_config:

    def __init__(self, config=None):
        self.config = config if config else self.load_config()
 
    def load_config(self):
        """
        Reads the configuration file and loads it in to the program, then returns to a local variable for 
        easy access to the varaiables in the config file.
        """
        try:
            with open('config.json', 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            logging.error("Configuration file 'config.json' not found.")
        except json.JSONDecodeError:
            logging.error("Configuration file 'config.json' is invalid JSON.")
        return None

    def raw_to_universal_path(self, raw_path):
        """
        Takes a path from config file and sets it to a universal os and returns the new value.
        
         Args:
            - Raw_path: Any given path not os specific 
        
         Returns:
            - Universal Path: A modified version of the inputed path that works any os.
         """
        return Path(self.config.get(raw_path))