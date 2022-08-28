import logging

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fhandler = logging.FileHandler(filename='app.log', mode='a')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.DEBUG)

shandler = logging.StreamHandler()
shandler.setFormatter(formatter)
shandler.setLevel(logging.INFO)


logger.addHandler(fhandler)
logger.addHandler(shandler)


logger.setLevel(logging.DEBUG)




