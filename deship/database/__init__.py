import rethinkdb as r


def get_connect():
    return r.connect()
