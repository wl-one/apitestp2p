from app import init_config
import logging

init_config()
logging.info('info')
logging.error('error')
logging.debug('debug')