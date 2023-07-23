#!/usr/bin/python3
"""
This module defines a Flask web app that displays the message "Hello HBNB!"

Routes:
    /: Display the message "Hello HBNB!"
"""

from flask import Flask, render_template

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

@app.route('/python/<text>', strict_slashes=False)
def display_text(text='is cool'):
    """
    Displays 'Python' followed by the value of the text variable

    Returns:
        str: Displays "Python" followed by the value of text and replaces '_' with
             ' '
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """
    Displays a number if its only an integer

    Args:
        n (int): The number as an argument

    Returns:
        str: 'n' followed by 'is a number'
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with the number if it's an integer.

    Args:
        n (int): The number passed in the URL

    Returns:
        str: The rendered HTML page with the number
    """
    return render_template('number_template.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """
    Displays a HTML page only if n is an integer

    Args:
        n (int): The number passed in the url

    Returns:
        str: The rendered HTML page with the number
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
