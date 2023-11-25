import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.gmail.com'  # Gmail's SMTP server
smtp_port = 587  # SMTP port for TLS
smtp_username = 'linuscodes56@gmail.com'  # Your Gmail email address
smtp_app_password = ''  # App Password for Gmail
receiver_email = 'sunilkumar333221@gmail.com'  # Recipient's email address
subject = 'PC Started Notification'

# alias email
alias_email = 'System.mail@gmail.com'
alias_name = 'System Admin'

# Create the email message
message = MIMEMultipart()
message['From'] = f'{alias_name} <{alias_email}>'
# message['From'] = smtp_username
message['To'] = receiver_email
message['Subject'] = subject

text = "Someone is using your PC"

# Attach the text message
message.attach(MIMEText(text, 'plain'))

# Connect to Gmail's SMTP server
try:
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_app_password)

    # Send the email
    smtp.sendmail(smtp_username, receiver_email, message.as_string())
    print("Email sent successfully!")

    # Close the connection
    smtp.quit()
except Exception as e:
    print(f"Error: {str(e)}")
