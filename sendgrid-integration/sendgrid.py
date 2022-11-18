# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='varunkrishnan0001@gmail.com',
    to_emails='nandhakumarm26052002@gmail.com',
    subject='Job Recommendation from Jobby',
    html_content='<strong>Hello Nandhakumar! We found some jobs for you. Login to jobby to apply</strong>'
)
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)