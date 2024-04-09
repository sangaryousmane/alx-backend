#!/usr/bin/env python3
""" Main Flask app
"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

def hello():
    """ Simple route
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
