import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='varunkrishnan0001@gmail.com',
    to_emails='varunkrishnan.tech@gmail.com',
    subject='Job Recommendation',
    html_content='<strong>Hello varun we have some recommedations for you to apply for job. Check out now in the website</strong>')

sg = SendGridAPIClient("os.environ.get('SENDGRID_API_KEY')")
response = sg.send(message)
print(response.status_code, response.body, response.headers)
