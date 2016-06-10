from flask import render_template

from . import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('app_main.html')


@app.route('/setting')
def setting():
    return render_template('app_setting.html')


@app.route('/add_device')
def add_device():
    return render_template('add_device.html')


@app.route('/rule')
def rule():
    return render_template('rule.html')
