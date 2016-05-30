import json
from . import app
from flask import request
from deship.database import device
from deship.database import user


@app.route('/reg_device', methods=['POST'])
def regDevice():
    deviceInfoList = device.getAllDevice()
    userlist = user.getAllUser()
    cur_device = request.json
    user_finded = 0

    for i in deviceInfoList:
        device_curDict = json.loads(i)
        if cur_device['device_ID']==device_curDict['device_ID']:
            return 'Device already in list', 405
    for i in userlist:
        user_curDict = json.loads(i)
        if cur_device['user_ID']==user_curDict['ID']:
            user_finded = 1
    if user_finded == 0:
        return 'User not in list', 405

    device.addDeviceInfo(cur_device)
    return 'Success device registration'

@app.route('/device_list')
def printDeviceList():
    devicelist = device.getAllDevice()
    str_device=""
    for i in devicelist:
        str_device+=i
    return str_device

