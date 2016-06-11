from flask import jsonify

from . import app

from deship.database import item


@app.route('/item/<device_id>', methods=['GET'])
def get_item_list(device_id):
    items = item.get_item_list(device_id)
    return jsonify(itemlist=items)


@app.route('/item/<item_id>/img', methods=['GET'])
def get_item_image(item_id):
    img = item.get_item_image(item_id)
    import flask
    response = flask.Response(img)
    response.headers['Content-Type'] = "image/jpeg"
    response.headers['Content-Disposition'] = "inline; filename=item.jpg"
    return response
