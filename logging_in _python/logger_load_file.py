import logging
import logging.config

"""
Load config file
"""

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.debug('This is a debug message')


