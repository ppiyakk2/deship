from flask import json, jsonify, request
from . import app
from deship.database import transaction


@app.route("/transaction", methods=['GET'])
def transactions():
    st = transaction.get_my_transaction()
    return jsonify(transactiondata=st)


@app.route('/transaction/<tx_id>', methods=['GET'])
def get_transaction(tx_id):
    tx = transaction.get_transaction_detail(tx_id)
    return jsonify(transaction=tx)

@app.route('/transaction/<tx_id>/done', methods=['GET'])
def done(tx_id):
    transaction.done(tx_id)
