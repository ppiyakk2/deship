import json


def addUserInfo(userinfo):
    f = open("/home/pi/deship/deship/user_Info.txt", 'a')
    f.write(json.dumps(userinfo))
    f.write("\n")
    f.close()
    return 'good'

def getAllUser():
    l = None
    with open("/home/pi/deship/deship/user_Info.txt", 'r') as f:
        l = json.load(f)
    return l
