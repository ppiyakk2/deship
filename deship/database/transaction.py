import rethinkdb as r

from deship.config import cooperation_id


def get_my_transaction():
    con = r.connect(host='printf.kr', port=28015)
    return list(r.db('gyunggido').table('transaction').filter({'to': cooperation_id}).run(con))


def done(tx_id):
    con = r.connect(host='printf.kr', port=28015)
    r.db('gyunggido').table('transaction').get(tx_id).update({'request_done': True}).run(con)


def get_transaction_detail(tx_id):
    con = r.connect(host='printf.kr', port=28015)
    trans = r.db('gyunggido').table('transaction').get(tx_id).run(con)

    data = dict()
    data['request_time'] = trans['request_tx']
    data['address'] = trans['address']
    data['tx_id'] = trans['tx_id']

    # item info
    item_name = r.db('gyunggido').table('cooperation_item').get(trans['item_id']).pluck('name').run(con)['name']
    data['item_name'] = item_name

    # device info
    scon = r.connect(host='192.168.0.24', port=28015)
    d = r.db('service_provider').table('devices').get(trans['device_id']).run(scon)
    data['device_sn'] = d['SN']
    data['device_name'] = d['device_name']
    data['device_date'] = d['productive_date']

    # userinfo
    user_name = r.db('service_provider').table('users').get(trans['from']).pluck('user_name').run(scon)['user_name']

    data['user_name'] = user_name

    return data

