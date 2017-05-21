from flask import Flask
import requests

app=Flask(__name__)

@app.route('/')
def index():
	return "HI"

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.data
        print (result)
        return render_template("result.html",result = result)
