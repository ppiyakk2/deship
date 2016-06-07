from flask import request, jsonify

from deship.database import cooperation
from deship.database.models import Cooperations
from . import app


@app.route("/cooperation", methods=['POST'])
def coop():
    curcoop = request.values
    cooperation.save(curcoop)
    return "good"


@app.route("/cooperation", methods=['GET'])
def get_coops():
    return jsonify(cooperations=Cooperations.select_all())


@app.route("/cooperation/<coop_ID>/telehash", methods=['GET'])
def telehashfile(coop_ID):
    import flask
    priv_key = Cooperations.select_pk_by_id(coop_ID)
    response = flask.Response(priv_key)
    response.headers['Content-Type'] = "application/octet-stream"
    response.headers['Content-Disposition'] = "inline; filename=seed_id"
    return response
