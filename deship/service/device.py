from flask import request, jsonify

from . import app
from deship.database import device, monitor


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

    return jsonify(device=d)


@app.route('/device', methods=['GET'])
def get_devices():
    if 'user_id' not in request.cookies:
        return 'Login Required', 400

    devices = device.list_devices()
    return jsonify(devices=devices)


@app.route('/device/<serial_no>/status', methods=['GET'])
def get_device_status(serial_no):
    value = monitor.get_sensor_data(serial_no)

    amount = 0
    power = 0
    if value is not None:
        power = 1
        amount = round(value, 2)

    return jsonify(device_status={'power': power, 'amount': amount})


@app.route('/device/<serial_no>/alarm', methods=['GET'])
def get_device_alarm(serial_no):
    alarm = monitor.check_alarm(serial_no)
    return jsonify(alarm=alarm)
