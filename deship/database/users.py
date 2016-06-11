from datetime import datetime

from . import service_db, local_db


def add_user(data):
    db, con = service_db()
    data['reg_date'] = str(datetime.now())
    re = db.table('users').insert(data).run(con)

    if re['inserted'] != 1:
        return False

    ldb, lcon = local_db()
    ldata = {'item_key': 'city', 'city': data['address'].split(' ')[0]}
    ldb.table('assets').insert(ldata).run(lcon)
    return True


def get_user(user_id):
    db, con = service_db()
    re = db.table('users').get(user_id).pluck('user_name').run(con)
    return re['user_name']


def diff_password(data):
    db, con = service_db()
    re = db.table('users').get(data['ID']).pluck('passwd').run(con)

    if re is None:
        return False, None

    if data['passwd'] == re['passwd']:
        return True
    else:
        return False
