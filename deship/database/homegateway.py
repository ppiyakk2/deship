import time
import rethinkdb as r

from deship.config import city_database


def join(data):
    con = r.connect()

    # TODO check validation of device id
    device = get(data['device_id'], con)
    now = time.time()
    if device is None:
        data['join_timestamp'] = now
        data['online_timestamp'] = now
        data['is_node'] = False
        del data['join']
        save(data, con)
        con.close()
        return True

    if data['join'] == '1':
        update(data['device_id'], now, data['public_ip'], con, now)
    else:
        update(data['device_id'], now, data['public_ip'], con)
    con.close()


def update(device_id, ot, ip, con, jt=None):
    update_field = dict()
    update_field['online_timestamp'] = ot
    update_field['public_ip'] = ip
    if jt is not None:
        update_field['join_timestamp'] = jt
    r.db(city_database).table('homegateway').get(device_id)\
        .update(update_field).run(con)


def save(device, con):
    r.db(city_database).table('homegateway').insert(device).run(con)


def get(device_id, con=None):
    return r.db(city_database).table('homegateway').get(device_id).run(con)