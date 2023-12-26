from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser()
    config.read("SeleniumBDD\\Utilities\\config.ini")
    return config.get(section, key)
