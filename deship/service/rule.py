from flask import request, jsonify

from . import app
from deship.database import rule


@app.route('/rule/<device_id>', methods=['POST'])
def add_device_rule(device_id):
    values = request.values
    rule.add_device_rule(device_id, values)
    return ''


@app.route('/rule/<device_id>', methods=['GET'])
def get_device_rule(device_id):
    device_rule = rule.get_device_rule(device_id)
    if device_rule is None:
        return 'No device', 404
    return jsonify(rule=device_rule)

