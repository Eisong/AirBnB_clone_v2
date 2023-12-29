#!/usr/bin/python3
"""Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strick_slashes=Flash)
def hello_hbnb():
	""" Display 'Hello HBNB!'. """
	return "HBNB"
if __name__ == "__main__":
	# Start the Flask develoment server
	# Listen on all available network interfaces (0.0.0.0) and port 5000
	app.run(host='0.0.0.0', port=5000)
