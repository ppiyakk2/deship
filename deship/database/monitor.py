from . import local_db, city_db, service_db
import time


def save_sensor_data(device_id, value, alarm=True):
    db, con = local_db()
    data = {'device_id': device_id, 'value': value,
            'last_updated': time.time(), 'alarm': False, 'checked': False}

    sd = db.table('sensor_data').get(device_id).run(con)

    if sd is None:
        db.table('sensor_data').insert(data).run(con)

    if not alarm and sd['alarm']:
        data['alarm'] = False
        data['checked'] = False
    elif alarm:
        data['alarm'] = True
        data['checked'] = sd['checked']

    db.table('sensor_data').get(device_id)\
        .update({'value': value, 'last_updated': time.time(),
                 'alarm': data['alarm'], 'checked': data['checked']}).run(con)


def check_alarm(device_id):
    db, con = local_db()

    sd = db.table('sensor_data').get(device_id).run(con)

    if sd['alarm'] and not sd['checked']:
        db.table('sensor_data').get(device_id).update({'checked': True}).run(con)
        return True
    return False


def get_sensor_data(device_id):
    db, con = local_db()

    sd = db.table('sensor_data').get(device_id).run(con)

    if sd is None:
        return None

    time_diff = time.time() - sd['last_updated']

    if time_diff > 5:
        return None

    return sd['value']


def is_ordered(device_id, item_id):
    db, con = local_db()
    try:
        ret = db.table('assets')\
            .filter({'item_key': 'ordered', 'device_id': device_id,
                     'item_id': item_id}).run(con)
    except Exception:
        return False

    if len(list(ret)) == 0:
        return False
    else:
        return True


def delete_ordered_record(device_id, item_id):
    db, con = local_db()
    db.table('assets')\
        .filter({'item_key': 'ordered', 'device_id': device_id,
                 'item_id': item_id}).delete().run(con)


def do_order(device_id, item_id):
    from datetime import datetime

    tx_data = {'from': '', 'to': '', 'item_id': item_id, 'device_id': device_id,
               'request_tx': str(datetime.now()), 'request_done': False, 'address': ''}

    db, con = local_db()

    user_id = db.table('assets').get('user_id').run(con)['user_id']
    tx_data['from'] = user_id

    cdb, ccon = city_db()
    cooper_id = cdb.table('cooperation_item').get(item_id).pluck('co_id').run(ccon)['co_id']
    tx_data['to'] = cooper_id

    sdb, scon = service_db()
    address = sdb.table('users').get(user_id).pluck('address').run(scon)['address']
    tx_data['address'] = address

    cdb.table('transaction').insert(tx_data).run(ccon)

    d = {'item_key': 'ordered', 'device_id': device_id, 'item_id': item_id}
    db.table('assets').insert(d).run(con)
