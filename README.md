#README for email_writer.py

This Python script sends emails to a list of recipients using Gmail API.
Dependencies

This script requires the following dependencies:

    pandas
    google-auth
    google-auth-oauthlib
    google-auth-httplib2
    google-api-python-client

All of the above packages can be installed using pip.
Usage

    Create a Google Cloud Console project and enable the Gmail API by following the instructions here: https://developers.google.com/gmail/api/quickstart/python?hl=de.
    Download the client configuration file (credentials.json) from the Google Cloud Console and place it in the same directory as email_writer.py.
    Create a CSV file containing the list of email addresses to which the emails will be sent. Make sure that the file contains a column named "Email Address". The script will only send emails to those email addresses which have an empty "Contacted" column.
    Update the subject and body of the email in the email_writer.py script.
    Run the script using python email_writer.py. If this is the first time you are running the script, it will ask you to authorize the application using your Google account. Follow the instructions to do so.
    The script will send emails to all the email addresses in the CSV file which have an empty "Contacted" column. The script will update this column to indicate that an email has been sent to that email address.

Notes

    The script uses token.json to store the OAuth2 credentials. If you want to use a different file name, make sure to update the code accordingly.
    The script will only send emails to those email addresses which have an empty "Contacted" column in the CSV file. If you want to change this behavior, you will need to modify the script.
    The script sends plain text emails. If you want to send HTML emails, you will need to modify the code to use MIMEText('html') instead of MIMEText('plain').
