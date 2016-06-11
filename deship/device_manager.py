import os

from deship.lib.logger import Logger, init_logger

init_logger()


def run():
    pid = os.fork()
    if pid == 0:
        Logger.common_logger.info('Starting Device Manager')
        while True:
            print 'hello'
            import time
            time.sleep(1)
    else:
        return pid
