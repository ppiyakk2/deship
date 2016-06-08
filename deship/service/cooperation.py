from flask import request

from . import app
from deship.database import cooperation


@app.route('/party', methods=['POST'])
def add_cooperation():
    data = request.values
    cooperation.save(data)
    return 'done'
