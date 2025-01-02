import logging

def setup_logger(name='application.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
