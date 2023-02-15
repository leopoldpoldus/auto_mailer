import os
import base64
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

# Load email addresses from the xlsx file
df = pd.read_csv("email_list.csv")
email_list = df[df['Contacted'].isnull()]['Email Address'].tolist()

# Set up the Gmail API client
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# Send emails to the list of email addresses
for email in email_list:
    try:
        message = MIMEMultipart()
        message['to'] = email
        message['subject'] = "mail subject"
        body = """mail body"""
        message.attach(MIMEText(body, 'plain'))
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {email} Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
