import logging

def getLogger(logger_name: str = "basicLogger"):

    # create logger
    logger = logging.getLogger('CustomLog\t{}'.format(logger_name.split('.')[-1]))
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(name)s \t%(levelname)s  \t%(asctime)s \n%(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger

