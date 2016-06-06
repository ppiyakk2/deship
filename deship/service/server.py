import os
from . import app

from deship.lib.logger import Logger, init_logger

init_logger()


def run_service():
    pid = os.fork()
    if pid == 0:
        Logger.service_logger.info('Starting Service Web Server')
        app.run(host='0.0.0.0', port=8080)
    else:
        return pid
