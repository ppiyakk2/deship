from . import local_db


def add_device_rule(device_id, data):
    db, con = local_db(debug=True)
    exist = db.table('device_rule').get(device_id).run(con)

    rule = {
        'device_id': device_id,
        'rule': data
    }
    if exist is None:
        db.table('device_rule').insert(rule).run(con)
    else:
        db.table('device_rule').update({'rule': data}).run(con)


def get_device_rule(device_id):
    db, con = local_db(debug=True)
    ret = db.table('device_rule').get(device_id).run(con)
    if ret is None:
        return None
    return ret['rule']
