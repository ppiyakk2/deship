import rethinkdb as r

from . import get_connect


class City:
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    def save(self):
        con = get_connect()
        d = self.__dict__
        r.db('service_provider').table('cities').insert(d).run(con)


class Device:
    def __init__(self, sn, name, dtype, productive_date, user_id):
        self.sn = sn
        self.name = name
        self.device_type = dtype
        self.productive_date = productive_date
        self.user_id = user_id

