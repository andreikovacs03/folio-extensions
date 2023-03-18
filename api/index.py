from flask import Flask
from api import libgen

app = Flask(__name__)

app.register_blueprint(libgen.views.blueprint)
