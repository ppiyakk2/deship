import json


def addCityInfo(cityinfo):
    f = open("city_Info.txt", 'a')
    f.write(json.dumps(cityinfo))
    f.write("\n")
    f.close()
    return 'good'

def getAllCity():
    list= []
    f = open("city_Info.txt", 'r')
    while True:
        str =f.readline()
        if not str: break
        list.append(str)
    return list