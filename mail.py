import smtplib

gmail_user = 'attendance.service.upt@gmail.com'  
gmail_password = 'Sdsdsd12'

sent_from = gmail_user  
to = ['attendance.service.upt@gmail.com', 'andreiburuntia@gmail.com']  

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, "hello")
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')