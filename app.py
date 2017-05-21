from flask import Flask
from flask import request
import smtplib

gmail_user = 'attendance.service.upt@gmail.com'  
gmail_password = 'Sdsdsd12'

sent_from = gmail_user  
to = ['attendance.service.upt@gmail.com', 'andreiburuntia@gmail.com']  

app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/mail')
def mail_it():
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, "hello")
        server.close()

        print ('Email sent!')
    except:  
        print ('Something went wrong sending email...')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    print("ASDASDASDAS")
    if request.method == 'POST':
        result = request.data
        d=(str(result)).split(" ")
        return d[0]+"\n"+d[1]

if __name__ == '__main__':
    app.run(debug=True)