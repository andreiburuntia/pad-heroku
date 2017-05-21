from flask import Flask
import requests

app=Flask(__name__)

@app.route('/')
def index():
	return "HI"

@app.route('/result',methods = ['POST', 'GET'])
def result():
    return request
