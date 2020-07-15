# To access environment variables (Api Key) in Windows
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SENDGRID_API_KEY')


def send_mail(request):
        
    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    #import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    # To access environment variables (Api Key) in Windows
    # from dotenv import load_dotenv
    # load_dotenv()

    # import Abort function from Flask
    from flask import abort

    # Verify request JSON
    # silent= True sets the var to none, if no json object is present
    request_json = request.get_json(silent=True)

    # Tuple of email params
    parameters = ('sender', 'receiver', 'subject', 'message')

    # initialize variables as empty strings
    sender, receiver, subject, message = '', '', '', ''

    # check if there is data in the request_json (check if all params in request_json)
    if request_json and all(k in request_json for k in parameters):
        sender = request_json['sender']
        receiver = request_json['receiver']
        subject = request_json['subject']
        message = request_json['message']
    else:
        abort(400) # 400 Bad Request Status Code

    # Set Mail Object
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message
    )

    # Sendgrid API request
    try:
        #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg = SendGridAPIClient(api_key)
        sg.send(message)
        return 'OK', 200 # 200 OK Status Code
    except Exception as e:
        return e, 400 # error msg and 400 Bad Request Status Code 
    



