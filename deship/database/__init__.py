import rethinkdb as r


def get_connect():
    return r.connect(host='211.198.65.241')
