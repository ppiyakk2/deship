import json
from . import app
from flask import request
from deship.database import city


@app.route('/reg_city', methods=['POST'])
def regCity():
    cityInfoList = city.getAllCity()
    cur_city = request.json

    for i in cityInfoList:
        city_curDict = json.loads(i)
        if cur_city['city_name']==city_curDict['city_name']:
            return 'City already existed in list', 405

    city.addCityInfo(cur_city)
    return 'Success City registration'

@app.route('/city_list')
def printCityList():
    citylist = city.getAllCity()
    str_city=""
    for i in citylist:
        str_city+=i
    return str_city

