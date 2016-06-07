import json
from . import app
from deship.database import user
from deship.database.models import Device
from flask import request, jsonify


@app.route('/reg_user', methods=['POST'])
def regUser():
    userList = user.getAllUser()
    cur_user = request.json

    for i in userList:
        curDict = json.loads(i)
        if cur_user['ID']==curDict['ID']:
            return 'ID already exist in system', 405

    user.addUserInfo(cur_user)
    return 'Success User registration'


@app.route('/users')
def printUserList():
    userlist = user.getAllUser()
    return jsonify(userlist=userlist)


@app.route('/users/<user_id>')
def userinfo(user_id):
    u = user.get_user_by_id(user_id)
    return jsonify(user=u)


@app.route('/users/<user_id>/devices', methods=['GET'])
def userdevicelist(user_id):
    a = Device.select_by_user(user_id)
    return jsonify(devicelist=a)
