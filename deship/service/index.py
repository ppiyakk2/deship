# -*- coding: utf-8 -*-

from flask import render_template

from . import app
from deship.database import device


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('app_main.html')


@app.route('/setting/<device_id>')
def setting(device_id):
    return render_template('app_setting.html', device_id=device_id)


@app.route('/add_device')
def add_device():
    return render_template('add_device.html')


@app.route('/rule/<device_id>/page')
def rule(device_id):
    dev = device.get_device(device_id)
    return render_template('rule.html', device_id=device_id,
                           device_name=dev['device_name'])
