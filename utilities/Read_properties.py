# lets see how to read data from ini file
import configparser

config = configparser.RawConfigParser()
config.read("/Users/pranjalnama/PycharmProjects/nopcommereApp/Configurations/config.ini")


# only read the config.ini noq how we can get the values

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        Url = config.get('common', 'baseURL')
        return Url

    @staticmethod
    def getApplicationUseremail():
        usrnme = config.get('common', 'useremail')
        return usrnme

    @staticmethod
    def getApplicationPassword():
        passwd = config.get('common', 'password')
        return passwd
