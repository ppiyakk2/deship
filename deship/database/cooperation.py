import requests

from deship.messaging import gentool
from deship.database.models import Cooperations, City


def save(co):
    hn, priv = gentool.generate()
    c = Cooperations(hn, co['name'], co['city_id'], co['category'],
                     priv)
    c.save()

    city = City.select_by_id(co['city_id'])
    save_to_city(city['url'], c)


def save_to_city(city_url, city):
    url = "%s/party" % city_url
    data = {'name': city.name, 'telehash_id': city.id,
            'category': city.category}
    r = requests.post(url, data=data)

