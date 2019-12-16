import os
import logging

path = os.path.dirname(os.path.realpath(__file__))
log_file = 'log.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(path + '\\' + log_file)
    ])

logging.critical('msg')
logging.error('msg')
logging.warning('msg')
logging.info('msg')
logging.debug('msg')
