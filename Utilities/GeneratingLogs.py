import logging

'''
logging.basicConfig(filename="C:\\Users\\pmrig\\OneDrive\\Desktop\\PDevelopment\\Development\\Selenium+BDD\\SeleniumBDD\\Utilities\\Logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logger = logging.getLogger()
logger.info("This is my First log")
'''

def log():
    logging.basicConfig(filename="C:\\Users\\pmrig\\OneDrive\\Desktop\\PDevelopment\\Development\\Selenium+BDD\\SeleniumBDD\\Utilities\\Logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logger = logging.getLogger()
    return logger 

logging = log()
logging.info("This is my second entry")
logging.error("This is an error message")
