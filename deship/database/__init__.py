import rethinkdb as r

from deship.config import database as db


def local_db(debug=False):
    if debug:
        con = r.connect(host=db['service_domain'], port=db['service_port'])
        rdb = r.db('home1')
    else:
        con = r.connect()
        rdb = r.db('home')
    return rdb, con


def city_db():
    con = r.connect(host=db['city_domain'], port=db['city_port'])
    rdb = r.db('gyunggido')
    return rdb, con


def service_db():
    con = r.connect(host=db['service_domain'], port=db['service_port'])
    rdb = r.db('service_provider')
    return rdb, con
