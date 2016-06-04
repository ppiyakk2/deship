import json
from . import app
from deship.database import user
from deship.database import city
from flask import request, jsonify

@app.route('/reg_user', methods=['POST'])
def regUser():
    userList = user.getAllUser()
    cur_user = request.json


    for i in userList:
        curDict = json.loads(i)
        if cur_user['ID']==curDict['ID']:
            return 'ID already exist in system', 405
    '''for i in cityList:
        city_curDict = json.loads(i)
        if cur_user['city_name'] == city_curDict['city_name']:
            city_finded = 1
    if city_finded == 0:
        return 'City not exist in list', 405'''

    user.addUserInfo(cur_user)
    return 'Success User registration'

@app.route('/user_list')
def printUserList():
    userlist = user.getAllUser()
    return jsonify(userlist=userlist)

@app.route('/user_info')
def userinfo():
    userlist = user.getAllUser()
    return jsonify(userlist=userlist)


@app.route('/user_devlist/<user_id>', methods=['GET'])
def userdevicelist(user_id):
    print user_id
    a = [{"SN": "NF523TG5", "device_name": "R570", "device_type": "Laundry", "productive_date": "2016-06-02"},
        {"SN": "GRO1245", "device_name": "Y5", "device_type": "Fan", "productive_date": "2016-01-02"},
        {"SN": "GOE3021", "device_name": "UHDTV", "device_type": "TV", "productive_date": "2016-03-02"}]
    return jsonify(devicelist=a)
