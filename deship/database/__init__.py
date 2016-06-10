import rethinkdb as r

from deship.config import database as db


def local_db():
    return r.connect()


def city_db():
    return r.connect(host=db['city_domain'], port=db['city_port'])


def service_db():
    return r.connect(host=db['service_domain'], port=db['service_port'])
