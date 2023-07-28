import logging
exc_logger = logging.getLogger()
exc_logger.setLevel('ERROR')
file_hander = logging.FileHandler('logger_notfication_bot.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s - %(message)s')
file_hander.setFormatter(formatter)
exc_logger.addHandler(file_hander)


