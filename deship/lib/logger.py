import logging
import logging.config

import deship.config as settings


class Logger:
    db_logger = None
    telehash_logger = None
    service_logger = None
    common_logger = None

    def __init__(self):
        pass


def init_logger():
    logging.config.dictConfig(settings.logging)
    Logger.db_logger = logging.getLogger('database')
    Logger.telehash_logger = logging.getLogger('telehash')
    Logger.service_logger = logging.getLogger('service')
    Logger.common_logger = logging.getLogger('common')
