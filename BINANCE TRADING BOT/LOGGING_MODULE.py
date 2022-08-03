import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formater = logging.Formatter(f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
streamHandler.setFormatter(formater)
streamHandler.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)


file_hander = logging.FileHandler('/Users/aleksei.semerikov/PycharmProjects/BINANCE TRADING BOT/logging_module.log')
file_hander.setLevel(logging.DEBUG)
file_hander.setFormatter(formater)
logger.addHandler(file_hander)



# logger.info('FOR INFORMATION')
# logger.debug('FOR DEBUG')
# logger.warning('WARNING')
# logger.error(('ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'))