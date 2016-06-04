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
    print id
    return jsonify(status=get_cluster_status())


@app.route('/city/<id>/throughput', methods=['GET'])
def city_cluster_throughput(id):
    print id
    return jsonify(throughput=get_cluster_throughput())


def get_cluster_status():
    url = 'http://211.198.65.241:58090/cluster/status'
    r = requests.get(url)
    return r.json()


def get_cluster_throughput():
    url = 'http://211.198.65.241:58090/cluster/throughput'
    r = requests.get(url)
    return r.json()

