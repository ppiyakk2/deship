from . import local_db
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


def do_order(device_id, item_id):
    # check already ordered
    pass