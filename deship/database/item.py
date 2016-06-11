from . import local_db, city_db


def get_item_list(device_id):
    ldb, lcon = local_db(debug=True)

    device_type = ldb.table('device').get(device_id).pluck('device_type').run(lcon)

    if device_type is None:
        return False

    cdb, ccon = city_db()
    items = cdb.table('cooperation_item').filter(device_type).run(ccon)
    return list(items) if items is not None else list()
