import configparser
import os

class ConfigLoader:
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(__file__), '..', config_file)
        
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
            
        self.config.read(self.config_path)

    def get_value(self, section, key):
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            raise ValueError(f"Configuration error: {str(e)}")

# Example usage:
# config = ConfigLoader()
# base_url = config.get_value('Environment', 'base_url')
