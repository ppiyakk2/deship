from . import app
from flask import render_template

@app.route('/')
def index():
    return render_template('provider_main.html')

@app.route('/provider_cityinfo')
def f():
    return render_template('provider_cityinfo.html')