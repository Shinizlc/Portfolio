import logging as log
logger =  log.getLogger()
stream = log.StreamHandler()
stream.setLevel(log.INFO)
formater = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream.setFormatter(formater)
logger.addHandler(stream)



