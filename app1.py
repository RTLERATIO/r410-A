from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
	return ("hello")

@app.route('/test')
def test():
	return ("test")
