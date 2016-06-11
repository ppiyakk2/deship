# -*- coding: utf-8 -*-

from flask import render_template, request

from . import app
from deship.database import device
from deship.database import users


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    user_id = request.cookies.get('user_id')
    name = users.get_user(user_id)
    return render_template('app_main.html', user_name=name)


@app.route('/setting/<device_id>')
def setting(device_id):
    user_id = request.cookies.get('user_id')
    name = users.get_user(user_id)
    return render_template('app_setting.html', device_id=device_id, user_name=name)


@app.route('/add_device')
def add_device():
    user_id = request.cookies.get('user_id')
    name = users.get_user(user_id)
    return render_template('add_device.html', user_name=name)


@app.route('/rule/<device_id>/page')
def rule(device_id):
    dev = device.get_device(device_id)
    return render_template('rule.html', device_id=device_id,
                           device_name=dev['device_name'])
