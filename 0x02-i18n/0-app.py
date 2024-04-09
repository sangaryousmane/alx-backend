#!/usr/bin/env python3
""" Main Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


Config = __import__("./1-app.py").Config
app = Flask(__name__, template_folder='templates')
babel = Babel(app)
app.config.from_object(Config)

@app.route("/", methods=['GET'], strict_slashes=False)
def hello():
    """ Simple route
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
