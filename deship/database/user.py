import json


def addUserInfo(userinfo):
    f = open("user_Info.txt", 'a')
    f.write(json.dumps(userinfo))
    f.write("\n")
    f.close()
    return 'good'

def getAllUser():
    list= []
    f = open("user_Info.txt", 'r')
    while True:
        str =f.readline()
        if not str: break
        list.append(str)
    return list