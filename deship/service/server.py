import os
from . import app


def run_service():
    pid = os.fork()
    if pid == 0:
        app.run(host='0.0.0.0', port=8090, debug=True)
    else:
        return pid