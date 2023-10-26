from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import routes  # Update "your_app" to the name of your Flask app directory
