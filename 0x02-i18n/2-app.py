#!/usr/bin/env python3
""" A module for local languages
"""
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_with_locale():
    """ Render hello with a language
    """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ Get the local language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
