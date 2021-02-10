from flask import Flask
from client import client as client_bp

app = Flask(__name__)
app.register_blueprint(client_bp)
