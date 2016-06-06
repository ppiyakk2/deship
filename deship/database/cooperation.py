import json


def getcoop():
    l = None
    with open("/home/pi/deship/deship/cooperation_list.txt", 'r') as f:
        l = json.load(f)
    return l