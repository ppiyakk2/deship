from flask import Flask

app = Flask(__name__)

import service.index
import service.cluster