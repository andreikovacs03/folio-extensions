from flask import Flask
from flask_cors import CORS
from api import libgen

app = Flask(__name__)
CORS(app)

app.register_blueprint(libgen.views.blueprint)
