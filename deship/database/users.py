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
    ldb, lcon = local_db()
    user_id = ldb.table('assets').get('user_id').run(lcon)['user_id']

    if user_id != data['ID']:
        return 2

    db, con = service_db()
    re = db.table('users').get(data['ID']).pluck('passwd').run(con)

    if re is None:
        return 0

    if data['passwd'] == re['passwd']:
        return 1
    else:
        return 0
