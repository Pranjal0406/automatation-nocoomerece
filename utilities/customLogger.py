import logging

class LogGen:
    @staticmethod
    def loggen():
        # Create logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Set logger level to INFO or any desired level

        # Create formatter
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Create file handler and set formatter
        file_handler = logging.FileHandler('/Users/pranjalnama/PycharmProjects/nopcommereApp/Logs/.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
