# This is start point of platform
import signal
import time
import os
import sys

from service import server as service_server
from messaging.server import TelehashServer
from config import init_config
from lib.logger import Logger, init_logger


service_pid = None
message_pid = None


def sigterm(signum, frame):
    global service_pid
    global message_pid

    if service_pid is not None:
        Logger.common_logger.info('Stopping Service')
        os.kill(int(service_pid), signal.SIGTERM)

    if message_pid is not None:
        Logger.common_logger.info('Stopping Telehash')
        os.kill(int(message_pid), signal.SIGTERM)
    sys.exit(1)

if __name__ == '__main__':
    init_config()
    init_logger()

    Logger.common_logger.info('Starting DESHIP Platform')

    service_pid = service_server.run_service()
    message_pid = TelehashServer().run()

    signal.signal(signal.SIGTERM, sigterm)
    signal.signal(signal.SIGINT, sigterm)

    while True:
        time.sleep(1)
