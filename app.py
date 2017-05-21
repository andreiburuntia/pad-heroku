from flask import Flask
import requests

app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/result',methods = ['POST', 'GET'])
def result():
    data = request.get_data()
    return data
