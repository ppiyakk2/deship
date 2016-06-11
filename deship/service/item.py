from flask import jsonify

from . import app

from deship.database import item


@app.route('/item/<device_id>', methods=['GET'])
def get_item_list(device_id):
    items = item.get_item_list(device_id)
    return jsonify(itemlist=items)
