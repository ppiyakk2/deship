import rethinkdb as r
from deship.config import city_database


def save(data):
    con = r.connect()
    r.db(city_database).table('cooperations').insert(data).run(con)
