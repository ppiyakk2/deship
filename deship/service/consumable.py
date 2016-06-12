from flask import jsonify, request, redirect, url_for
from . import app
from deship.database import consumable


@app.route("/consumable", methods=['POST'])
def add_consumable():
    cons = dict((key, request.form.getlist(key)[0]) for key in request.form.keys())
    image = request.files['image']
    consumable.add_consumable(cons, image)
    return redirect(url_for('.index'))


@app.route("/consumable", methods=['GET'])
def consumable_list():
    li = consumable.get_consumable_list()
    return jsonify(consumable=li)
