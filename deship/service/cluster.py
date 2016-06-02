from flask import jsonify

from . import app
from deship.database import cluster


@app.route('/cluster/status', methods=['GET'])
def cluster_status():
    total_nodes = len(cluster.get_all_servers())
    connected_nodes = len(cluster.get_connected_servers())
    utilized = (float(connected_nodes)/total_nodes) * 100
    return jsonify(
        total=total_nodes,
        connected=connected_nodes,
        utilized=utilized
    )

@app.route('/cluster/bootnode', methods=['GET'])
def get_bootnode():
    return 'bootnode'


@app.route('/cluster/throughput', methods=['GET'])
def get_throughput():
    r, w = cluster.get_throughput()
    return jsonify(
        read=r,
        write=w
    )
