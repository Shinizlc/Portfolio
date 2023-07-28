import logging as log
logger =  log.getLogger(__name__)
stream = log.StreamHandler()
stream.setLevel(log.DEBUG)
formater = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream.setFormatter(formater)
logger.addHandler(stream)

