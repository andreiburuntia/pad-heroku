from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return "HI"

@app.route('/req', methods=['GET','POST'])
	def respond():
		body=request.values.get('Body', None);
		print (body)
		return "got it"