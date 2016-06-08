from flask import Flask

app = Flask(__name__)

import service.index
import service.cooperation
import service.cluster
import service.homegateway
