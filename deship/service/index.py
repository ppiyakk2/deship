from . import app


@app.route('/')
def index():
    return "This is city area's distributed manager"
