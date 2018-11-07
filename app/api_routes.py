from app import app
import json
from flask import jsonify
from app import db

@app.route('/test')
def test_route():
	return "hello world"
