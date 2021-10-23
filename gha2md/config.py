from .singleton import SingletonMeta
import yaml


class ConfigManager(metaclass=SingletonMeta):
    def ConfigManager(self):
        self.verbose = 0
        self.config_file = ""

    def load(self, filepath):
        with open(filepath) as f:
            options = yaml.load(f, Loader=yaml.FullLoader)
