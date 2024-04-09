#!/usr/bin/env python3
""" Main Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    """ Simple route
    """
    return render_template("index.html", title="Welcome to Holberton")
