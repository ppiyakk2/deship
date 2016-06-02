import json
from . import app
from flask import request
from deship.database import device
from flask import jsonify


@app.route('/reg_device', methods=['POST'])
def regDevice():
    cur_device = request.json
    '''
    for i in deviceInfoList:
        device_curDict = json.loads(i)
        if cur_device['SN']==device_curDict['SN']:
            return 'Device already exist in list', 405
    '''
    device.addDeviceInfo(cur_device)
    return 'Success device registration'

@app.route('/device_list')
def printDeviceList():
    devicelist = device.getAllDevice()
    return jsonify(devicelist = devicelist)

