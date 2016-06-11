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
        return 'Already registered', 409

    return 'done'


@app.route('/device/<serial_no>', methods=['GET'])
def get_device_info(serial_no):
    if 'user_id' not in request.cookies:
        return 'Login Required', 400

    d = device.get_device(serial_no)

    if d is None:
        return 'No Device', 404

    if d['user_id'] is not None:
        return 'Already registered', 409

    return jsonify(device=d)


@app.route('/device', methods=['GET'])
def get_devices():
    if 'user_id' not in request.cookies:
        return 'Login Required', 400

    devices = device.list_devices()
    return jsonify(devices=devices)


@app.route('/device/<serial_no>/status', methods=['GET'])
def get_device_status(serial_no):
    return jsonify(device_status={'power': 1, 'amount': 50.5})
