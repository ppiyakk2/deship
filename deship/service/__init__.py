from flask import Flask

app = Flask(__name__)

from . import index
from . import user
from . import device
from . import city