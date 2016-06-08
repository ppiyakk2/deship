from flask import request

from . import app
from deship.database.homegateway import join

@app.route('/home_gateway', methods=['POST'])
def join_homegateway():
    data = dict((key, request.form.getlist(key)[0]) for key in request.form.keys())

    join(data)
    return 'done'
