from typing import Any
import yaml
from gha2md.helpers import singleton 


class ConfigManager(metaclass=singleton.SingletonMeta):
    def __init__(self, config=None):
        self.config_file = ""
        self.config = {
            "verbose": 0,
            "filter_patterns": ["sisifo_actions/**", "!**"],
            "no_color": False
        }
        if config:
            self.config = config

    def load(self, filepath):
        with open(filepath, encoding="utf-8") as file:
            options = yaml.load(file, Loader=yaml.FullLoader)
            if options:
                self.config.update(options)

    def get_config_value(self, key: str) -> Any:
        return self.config.get(key, None)

    def set_config_value(self, key, value):
        self.config[key] = value
