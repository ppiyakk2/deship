import json
from . import app
from deship.database import user
from deship.database import city
from flask import request

@app.route('/reg_user', methods=['POST'])
def regUser():
    userList = user.getAllUser()
    cityList = city.getAllCity()
    cur_user = request.json
    city_finded = 0


    for i in userList:
        curDict = json.loads(i)
        if cur_user['ID']==curDict['ID']:
            return 'ID already in system', 405
    for i in cityList:
        city_curDict = json.loads(i)
        if cur_user['city_name'] == city_curDict['city_name']:
            city_finded = 1
    if city_finded == 0:
        return 'City not in list', 405

    user.addUserInfo(cur_user)
    return 'Success User registration'

@app.route('/user_list')
def printUserList():
    userlist = user.getAllUser()
    str_user=""
    for i in userlist:
        str_user+=i
    return str_user
