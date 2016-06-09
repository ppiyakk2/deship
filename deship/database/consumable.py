import json

def add_consumable(consumable):
    with open("/home/vagrant/deship/deship/consumable.txt",'a') as f :
        f.write(json.dumps(consumable))

def get_consumable_list():
    with open("/home/vagrant/deship/deship/consumable.txt",'r') as f :
        s = json.load(f)
    return s