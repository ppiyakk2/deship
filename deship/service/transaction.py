from flask import json, jsonify, request
from . import app
from deship.database import transaction

@app.route("/transaction/save", methods = ['POST'])
def save_transaction():
    transac = request.json
    transaction.add_transaction(transac)
    return "good"

@app.route("/transaction/list", methods=['GET'])
def transactiondata():
    st = transaction.get_my_transaction()
    return jsonify(transactiondata = st)

@app.route("/transaction/<status>", methods=['GET'])
def completionstatus(status):
    s = transaction.get_my_transaction()
    comlist = list()
    onlist = list()
    for i in s :
        if i["status"] == "complete":
            comlist.append(i)
        if i["status"] == "ongoing" :
            onlist.append(i)

    if status == "complete" :
        return jsonify(status = comlist)
    elif status == "ongoing" :
        return jsonify(status = onlist)
    else :
        return "confirm url"
