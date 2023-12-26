from configparser import ConfigParser


'''
config = ConfigParser()
config.read("SeleniumBDD\\Utilities\\config.ini")
print(config.get("locator", "username"))
'''

def readConfig(section, key):
    config = ConfigParser()
    config.read("SeleniumBDD\\Utilities\\config.ini")
    return config.get(section, key)

print(readConfig("locator", "username"))