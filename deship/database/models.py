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

    @classmethod
    def select_by_id(cls, id):
        con = get_connect()
        return r.db('service_provider').table('cities').get(id).run(con)


class Device:
    def __init__(self, sn, name, dtype, productive_date, user_id=None):
        self.SN = sn
        self.device_name = name
        self.device_type = dtype
        self.productive_date = productive_date
        self.user_id = user_id

    def save(self):
        con = get_connect()
        d = self.__dict__
        r.db('service_provider').table('devices').insert(d).run(con)

    @classmethod
    def select_all(cls):
        con = get_connect()
        return list(r.db('service_provider').table('devices').run(con))

    @classmethod
    def select_by_user(cls, user_id):
        con = get_connect()
        return list(r.db('service_provider').table('devices')
                    .filter({'user_id': user_id}).run(con))


class User:
    def __init__(self):
        pass

    @classmethod
    def select_all(cls):
        con = get_connect()
        return list(r.db('service_provider').table('users').run(con))

    @classmethod
    def select_id(cls, id):
        con = get_connect()
        return r.db('service_provider').table('users').get(id).run(con)


class Cooperations:
    def __init__(self, cid, name, city_id, category, pk):
        self.id = cid
        self.name = name
        self.city_id = city_id
        self.category = category
        self.private_key = pk

    def save(self):
        con = get_connect()
        d = self.__dict__
        r.db('service_provider').table('cooperations').insert(d).run(con)

    @classmethod
    def select_pk_by_id(cls, id):
        con = get_connect()
        return r.db('service_provider').table('cooperations').get(id)\
            .get_field('private_key').run(con)

    @classmethod
    def select_all(cls):
        con = get_connect()
        return list(r.db('service_provider').table('cooperations')
                    .merge(lambda c: {'city_name': r.db('service_provider')
                           .table('cities').get(c['city_id'])
                           .pluck('name')['name']}).without('private_key')
                    .run(con))
