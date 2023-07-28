import logging
logger=logging.getLogger()
StreamLogger = logging.StreamHandler()
StreamLogger.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
StreamLogger.setFormatter(formater)
logger.addHandler(StreamLogger)