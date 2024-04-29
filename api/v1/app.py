#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# Create an instance of Flask
app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exception):
    """
    Method to handle app teardown. It closes the storage connection
    """
    storage.close()


if __name__ == "__main__":
    # Define host and port using environment variables or defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask server with specified host and port
    app.run(host=host, port=port, threaded=True)
