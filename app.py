"""
Simple server to display points of interests map of Eugene, OR
"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

import uuid
app.secret_key = str(uuid.uuid4())
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)

# For Favicon loading
import os

@app.route("/")
@app.route("/index")
def index():
  app.logger.debug("Main page entry")
  return flask.render_template('index.html')
  
@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
                               
@app.route('/_getPOI')
def get_poi():
	""" 
	Get the points of interest from 'poi.txt'
	Return dict
	"""
	rslt = {"locations": []}
	with open("poi.txt") as f:
		for line in f:
			line = line.split()
			lng = line.pop(-1)
			lat = line.pop(-1)
			name = " ".join(line)
			rslt["locations"].append((name,lat,lng))
	return jsonify(result=rslt)
				
	
###################
#   Error handlers
###################
@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return render_template('page_not_found.html'), 404
    
    
if __name__ == "__main__":
    # Standalone. 
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    app.debug=False