#!/usr/bin/env python3
""" Main Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello():
    """ Simple route
    """
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
