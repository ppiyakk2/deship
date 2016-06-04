import json
import rethinkdb as r

from . import get_connect


def add_city_info(cityinfo):

    return 'good'


def get_all_city():
    con = get_connect()
    return list(r.db('service_provider').table('cities').run(con))
