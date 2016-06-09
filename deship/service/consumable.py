from flask import json, jsonify, request
from . import app
from deship.database import consumable

@app.route("/consumable/add" , methods=['POST'])
def add_consumable ():
    cons = request.json
    consumable.add_consumable(cons)
    return "good"

@app.route("/consumable/list", methods=['GET'])
def consumable_list():
    li = consumable.get_consumable_list()
    return jsonify(transactiondata = li)