import json


def addDeviceInfo(deviceinfo):
    f = open("device_Info.txt", 'a')
    f.write(json.dumps(deviceinfo))
    f.write("\n")
    f.close()
    return 'good'

def getAllDevice():
    list= []
    f = open("device_Info.txt", 'r')
    while True:
        str =f.readline()
        if not str: break
        list.append(str)
    return list