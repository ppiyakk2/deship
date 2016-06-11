from . import local_db, service_db


def add_device(serial_no, user_id):
    db, con = service_db()
    device = db.table('devices').get(serial_no).run(con)

    if device is None:
        return 1

    if device['user_id'] is not None:
        return 2

    device['user_id'] = user_id
    db.table('devices').get(serial_no).update({'user_id': user_id}).run(con)

    ldb, lcon = local_db()
    ldb.table('device').insert(device).run(lcon)

    return 3


def list_devices():
    ldb, lcon = local_db()
    return list(ldb.table('device').run(lcon))


def get_device(serial_no):
    db, con = service_db()
    device = db.table('devices').get(serial_no).run(con)
    return device
