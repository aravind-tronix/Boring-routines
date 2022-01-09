#! /usr/bin/env python3

#Author : Aravind
#platform tested : windows and linux
#Python 3.2+
#Created on 08/01/2022
#email client

import imaplib
import email
from clientfuckedupagain.mailclient import sendmail
from clientfuckedupagain.pramikobaby import sshconnection
import schedule
import time


def incommingmail():
    #credentials
    username ="xxxxxx@gmail.com"        #your email

    # app password
    app_password= "xxxxxxx"             #password

    # For more >> https://www.systoolsgroup.com/imap/
    gmail_host= 'imap.gmail.com'        #gmail host

    #set connection
    mail = imaplib.IMAP4_SSL(gmail_host)

    #login
    log = mail.login(username, app_password)
    print(log)

    #select inbox
    mail.select("INBOX")
    n=0
    #select specific mails from specific user
    retcode, selected_mails = mail.search(None,'(UNSEEN)', '(FROM "xxxxxxx.com")') #reads unread email from specified email id(say clients)
    if retcode == 'OK':
        for num in selected_mails[0].split() :
          #print(num)
          print ('Processing ')
          n=n+1
          typ, data = mail.fetch(num,'(RFC822)')
          for response_part in data:
            if isinstance(response_part, tuple):
                original = email.message_from_bytes(data[0][1])
                print (original['From'])
                Subject = (original['Subject'])
                for part in original.walk():
                    if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                        message = part.get_payload(decode=True)
                        m = (message.decode())
                if  (Subject.find(('help') or ('trouble') or ('sorry'))!=-1) or (m.find(('help') or ('trouble') or ('sorry'))!=-1):
                    sshconnection()
                    sendmail()
                    typ, data = mail.store(num,'+FLAGS','\\Seen')
                else:
                    typ, data = mail.store(num,'-FLAGS','\\Seen')
            
schedule.every(10).minutes.do(incommingmail)     #check for incomming email every 10 minutes
while True: 
  schedule.run_pending() 
  time.sleep(1) 