import imaplib
import email

# Connect to the email server
imap_server = imaplib.IMAP4_SSL('imap.example.com')
imap_server.login('your_username', 'your_password')

# Select the inbox
imap_server.select('Inbox')

# Search for new emails
status, email_ids = imap_server.search(None, 'UNSEEN')
email_ids = email_ids[0].split()

# Iterate through the new emails
for email_id in email_ids:
    status, msg = imap_server.fetch(email_id, '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])

    # Process the email (e.g. print the subject and sender)
    print(f"Subject: {msg['Subject']}")
    print(f"From: {msg['From']}")

# Close the connection
imap_server.close()
imap_server.logout()
