#!/usr/bin/python3
"""
This module defines a Flask web app that displays the message "Hello HBNB!"

Routes:
    /: Display the message "Hello HBNB!"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display the message "Hello HBNB!" when the root URL is accessed.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello1_hbnb():
    """
    Displays the message "HBNB" when the URL is accessed.

    Returns:
        str: the sites name
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_text(text):
    """
    Displays 'C' followed by the value of text variable

    Returns:
        str: It displays the C after the text variable and replaces with _
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text(text="is cool"):
    """
    Displays 'Python' followed by the value of the text variable

    Returns:
        str: Displays "Python" then the value of text and replaces '_' with ' '
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
