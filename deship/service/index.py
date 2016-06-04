from . import app
from flask import render_template

@app.route('/')
def index():
    return render_template('provider_main.html')

@app.route('/provider_cityinfo/<city_id>')
def f(city_id):
    return render_template('provider_cityinfo.html', city_id=city_id)
