#!/usr/bin/python3
"""a flask web"""

from flask import Flask

app = Flask(__name__)

#define the route
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """dispaly hello hbnb"""
    return "Hello HBNB!"

if __name__ == "__main__":
    #start the flask
    app.run(host='0.0.0.0', port=5000)
