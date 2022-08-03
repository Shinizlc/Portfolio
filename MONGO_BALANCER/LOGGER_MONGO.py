import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
StreamLogger = logging.StreamHandler()
formatter = logging.Formatter(f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
StreamLogger.setFormatter(formatter)
#StreamLogger.setLevel(logging)
logger.addHandler(StreamLogger)