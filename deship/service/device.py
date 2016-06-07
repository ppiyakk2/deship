import json
from . import app
from flask import request
from deship.database import device
from flask import jsonify


@app.route('/reg_device', methods=['POST'])
def regDevice():
    device.addDeviceInfo(request.values)
    return 'Success device registration'


@app.route('/device_list')
def printDeviceList():
    devicelist = device.getAllDevice()
    return jsonify(devicelist=devicelist)

