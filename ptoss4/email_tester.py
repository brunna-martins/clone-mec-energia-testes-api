import requests
import json
import smtplib

database = {
    "brunna.louisemr@gmail.com",
    "brunna.louisemr@outlook.com",
    "pedroinjustice@gmail.com"
}

def valid_email(email): 

    url = 'https://emailvalidation.abstractapi.com/v1/?api_key=fc23e572e7124f3590f234b8ff030a30&email=%s' % (email)

    response = requests.get(url)

    myresponse = str(json.loads(response.content))

    if 'UNDELIVERABLE' in myresponse:
    
        return 'invalid email address'

    elif 'DELIVERABLE' in myresponse:
    
        return 'valid email address'
    
    else:

        return 'error'
    
    
def email_in_database(email):

   
    if email in database:

        return 'email address was found in database'
        
    else: 

        return 'could not find email address in database'
        
   

def reset_password(email):

    sender = "211029156@aluno.unb.br"
    receiver = email

    message = f"""\
    Subject: Reset Password
    To: {receiver}
    From: {sender}

    Reset your password with this link."""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as server:
        server.login("3a96ec0dfa1cdc", "c3a306fbfeebee")
        if server.sendmail(sender, receiver, message) == {}:
            return "email was sent successfully"
        else:
            return 'could not send email'
                    
    
 


    

