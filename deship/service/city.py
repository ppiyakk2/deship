import requests
from . import app
from flask import request, jsonify
from deship.database import city


@app.route('/city', methods=['GET'])
def get_city_list():
    citylist = city.get_all_city()
    return jsonify(citylist=citylist)


@app.route('/city/<id>/status', methods=['GET'])
def city_cluster_status(id):
    c = city.get_city_by_id(id)
    if c is None:
        return jsonify(msg="Wrong City ID"), 404
    return jsonify(status=get_cluster_status(c['url']))


@app.route('/city/<id>/throughput', methods=['GET'])
def city_cluster_throughput(id):
    c = city.get_city_by_id(id)
    if c is None:
        return jsonify(msg="Wrong City ID"), 404
    return jsonify(throughput=get_cluster_throughput(c['url']))


def get_cluster_status(city_url):
    url = '%s/cluster/status' % city_url
    r = requests.get(url)
    return r.json()


def get_cluster_throughput(city_url):
    url = '%s/cluster/throughput' % city_url
    r = requests.get(url)
    return r.json()

