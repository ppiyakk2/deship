from flask import jsonify

from . import app
from deship.database import cluster
from deship.config import bootnode_domain, bootnode_port


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
    data = {'domain': bootnode_domain, 'port': bootnode_port}
    return jsonify(bootnode=data)


@app.route('/cluster/throughput', methods=['GET'])
def get_throughput():
    r, w = cluster.get_throughput()
    return jsonify(
        read=r,
        write=w
    )
