from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/result',methods = ['POST', 'GET'])
def result():
    print("ASDASDASDAS")
    if request.method == 'POST':
        result = request.data
        d=(str(result)).split(" ")
        return d[0]+"\n"+d[1]

if __name__ == '__main__':
	app.run(debug=True)