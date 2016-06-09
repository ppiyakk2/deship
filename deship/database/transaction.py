import json

def add_transaction(transaction):
    with open("/home/vagrant/deship/deship/transaction.txt", 'a') as f :
        f.write(json.dumps(transaction))


def get_my_transaction():
    filename = "/home/vagrant/deship/deship/transaction.txt"
    s = None
    l = list()
    with open(filename,'r') as f :
        s = json.load(f)
    for i in s :
        if i["to"] == "hello":
            l.append(i)
    return l