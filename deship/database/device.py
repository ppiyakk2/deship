import json


def addDeviceInfo(deviceinfo):
    f = open("/home/pi/deship/deship/device_Info.txt", 'a')
    f.write(json.dumps(deviceinfo))
    f.write("\n")
    f.close()
    return 'good'


def getAllDevice():
    l = None
    with open("/home/pi/deship/deship/device_Info.txt", 'r') as f:
        l = json.load(f)
    return l
