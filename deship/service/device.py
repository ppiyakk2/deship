from flask import request, jsonify

from . import app
from deship.database import device


@app.route('/device', methods=['POST'])
def device_registration():
    data = request.values

    if 'user_id' not in request.cookies:
        return 'Login Required', 400

    user_id = request.cookies.get('user_id')
    re = device.add_device(data['SN'], user_id)
    if re == 1:
        return 'No device', 404
    elif re == 2:
        return 'Already registrated', 409

    return 'done'


@app.route('/device', methods=['GET'])
def get_devices():
    devices = device.list_devices()
    return jsonify(devices=devices)
