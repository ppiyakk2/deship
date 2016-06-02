import json
import rethinkdb as r

from . import get_connect


def addCityInfo(cityinfo):
    f = open("city_Info.txt", 'a')
    f.write(json.dumps(cityinfo))
    f.write("\n")
    f.close()
    return 'good'


def getAllCity():
    con = get_connect()
    return list(r.db('service_provider').table('cities').run(con))
