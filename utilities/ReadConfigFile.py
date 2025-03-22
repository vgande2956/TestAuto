from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(r'C:\Users\vinayg\PycharmProjects\pythonProject11\configurationfiles\data.ini')
    return config.get(section, key)