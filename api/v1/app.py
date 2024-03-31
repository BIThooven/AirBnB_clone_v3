#!/usr/bin/python3
"""app.py for the application"""
from flask import Flask, jsonify, Blueprint
from api.v1.views import app_views
from models import storage
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def teardown_app(code):
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    err = jsonify({"error": "Not found"}), 404
    return err


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
