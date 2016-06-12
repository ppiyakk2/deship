import base64
from flask import request, redirect, url_for

from . import app
from deship.database import users


@app.route('/users/signup', methods=['POST'])
def user_register():
    data = dict((key, request.form.getlist(key)[0]) for key in request.form.keys())
    if users.add_user(data):
        return 'ok'
    else:
        return 'ID Already Existed', 400


@app.route('/users/signin', methods=['POST'])
def user_login():
    data = request.values

    result = users.diff_password(data)
    if result == 1:
        response = app.make_response('ok')
        response.set_cookie('user_id', data['ID'])
        return response
    elif result == 0:
        return 'password not matched', 400
    elif result == 2:
        return 'not owner', 401
