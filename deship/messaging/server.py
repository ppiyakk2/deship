import os

from deship import plinth
from deship import config

config.init_config()


class TelehashServer:
    def __init__(self):
        id_key = self.__get_seed_id()
        self.server = plinth.Switch(listener=8090, key=id_key)

    def __get_seed_id(self):
        keyfile = config.telehash_conf_path + 'seed_id'
        with open(keyfile, 'r') as f:
            id_key = f.read()
        return id_key

    def run(self):
        pid = os.fork()
        if pid == 0:
            self.server.serve_forever()
        else:
            return pid

