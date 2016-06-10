from datetime import datetime

from . import service_db, local_db


def add_user(data):
    db, con = service_db()
    data['reg_date'] = str(datetime.now())
    re = db.table('users').insert(data).run(con)

    if re['inserted'] != 1:
        return False

    ldb, lcon = local_db(debug=True)
    ldata = {'item_key': 'city', 'city': data['address'].split(' ')[0]}
    ldb.table('assets').insert(ldata).run(lcon)
    return True


def diff_password(data):
    db, con = service_db()
    re = db.table('users').get(data['ID']).pluck('passwd').run(con)

    if data['passwd'] == re['passwd']:
        return True
    else:
        return False
