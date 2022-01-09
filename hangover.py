#Author : Aravind
#platform tested : windows and linux
#Python 3.2+
#Created on 08/01/2022
#Buy me a day off

from datetime import datetime
import schedule
import time
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from random import randrange
import os
from datetime import date




def sendmail():
	dates = ["09/01/2022","14/01/2022"] #specify dates to take a day off
	today = date.today()
	if today.strftime("%d/%m/%Y") in dates:
		my_lie_list = [
			"Hello Sir, I don’t think I’ll be able to make it to office today because my little child is very sick”. Don’t have children? You can use spouse for the same.", 
			"Are you crossing the line here? Don’t take this too seriously.Don’t hesitate to create a non existent old distant relative and make him dead due to natural causes.",
			"Your distance cousin is getting married and you can’t afford to miss that. Actually he came home to invite me personally.",
			"I can’t! I slipped in bathroom this morning. What to say! I had a knee injury. I don’t think I will be able to come on today."
		] 
		
		msg = my_lie_list[randrange(4)]
		print(msg)
		SMTP_HOST = 'imap.gmail.com'		#for more >> https://www.systoolsgroup.com/imap/
		SMTP_USER = 'xxxxxx@gmail.com'		#your email
		SMTP_PASS = 'xxxxxxxx'		#password

		# Craft the email by hand
		from_email = 'xxxxxx@gmail.com'  #simply the email address
		to_email = 'xxxxxx@gmail.com'
		body = msg.encode('ascii', 'ignore').decode('ascii')
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


def issession():
		ActiveConnections = os.popen('last -a | grep -i still').read() #gets only the active sessions
		if (ActiveConnections.find('slickdaddy') == -1): #my ssh username
			sendmail()


schedule.every().day.at("10:05").do(issession) #checks after the shift starts
while True: 
	schedule.run_pending() 
	time.sleep(1) 