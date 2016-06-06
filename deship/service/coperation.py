
import json
from . import app
from flask import Flask, request, jsonify, send_file, send_from_directory
from deship.database import cooperation

@app.route("/reg_cooperation", methods=['POST'])
def coop():
    curcoop = request.json
    with open("/home/pi/deship/deship/cooperation_list.txt", "a") as f :
        f.write(json.dumps(curcoop))
        f.write("\n")
    return "good"


@app.route("/coop_list")
def print_cooplist():
    cooplist = cooperation.getcoop()
    return jsonify(cooplist = cooplist)


@app.route("/<coop_ID>/telehash", methods=['GET'])
def telehashfile(coop_ID):
    return send_file("/home/pi/deship/deship/iu.jpg", as_attachment=True)
