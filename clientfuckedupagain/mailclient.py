#Author : Aravind
#platform tested : windows and linux
#Python 3.2+
#Created on 08/01/2022
#mail client to send mail via SMTP

from smtplib import SMTP_SSL, SMTP_SSL_PORT


def sendmail():
	SMTP_HOST = 'imap.gmail.com' #for gmail. For more >> https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html
	SMTP_USER = 'xxxxxx@gmail.com' #your email
	SMTP_PASS = 'xxxxxxxxxxx' #your password

	# Craft the email by hand
	from_email = 'xxxxxxx@gmail.com'  # simply the email address
	to_email = 'xxxxxxx@gmail.com'      #your email
	body = """Dear xxxxx,
		Whatever to butter the client"""
	headers = "From: {}".format(from_email)+"\r\n"
	# headers += "To: {}".format(to_email) 
	headers += "Subject: Hello"
	email_message = headers + "\r\n" + body
	# Connect, authenticate, and send mail
	smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
	smtp_server.set_debuglevel(1) 
	smtp_server.login(SMTP_USER, SMTP_PASS)
	smtp_server.sendmail(from_email, to_email, email_message)

	# Disconnect
	smtp_server.quit()