#!/usr/bin/python3
"""create endpoint status"""

from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify



@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns a JSON status
    """
    return jsonify({"status": "OK"})
