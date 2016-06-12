import json
import rethinkdb as r

from deship.config import cooperation_id


def add_consumable(item, image):
    con = r.connect(host='printf.kr', port=28015)
    item['co_id'] = cooperation_id
    item['image'] = r.binary(image.stream.read())
    r.db('gyunggido').table('cooperation_item').insert(item).run(con)


def get_consum(cid):
    con = r.connect(host='printf.kr', port=28015)
    re = r.db('gyunggido').table('cooperation_item').get(cid).pluck('image').run(con)
    return re['image']


def get_consumable_list():
    con = r.connect(host='printf.kr', port=28015)
    re = r.db('gyunggido').table('cooperation_item').filter({'co_id': cooperation_id}).without('image').run(con)
    return list(re) if re is not None else list()
