# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# this is used for constructing URLs to google's APIS
from googleapiclient.discovery import build

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

API_KEY = 'AIzaSyDhbRM4UUBRqouCvuTD-eNMTcdUx7ukN1k'
TABLE_ID = '1UvKGchZrRW4BR-bQ8hGzNu2U22Ab3lazVB7Rf2w'

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
service = build('fusiontables', 'v1', developerKey=API_KEY)

@app.route('/')
def hello():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()

@app.route('/about')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    return template.render()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
