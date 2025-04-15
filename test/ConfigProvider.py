import configparser


global_config = configparser.ConfigParser(interpolation=None)
global_config.sections()
global_config.read('config.ini')


class ConfigProvider:
    def __init__(self,):
        self.config = global_config

    def get(self,section: str, prop:str):
        return self.config[section].get(prop)

    def getint(self, section: str, prop: str):
        return self.config[section].getint(prop)