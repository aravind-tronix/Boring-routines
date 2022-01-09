#Author : Aravind
#platform tested : windows and linux
#Python 3.2+
#Created on 08/01/2022
#brew me a coffee

import time
import schedule
import os


def issession():
		ActiveConnections = os.popen('last -a | grep -i still').read() #gets only the active sessions
		if (ActiveConnections.find('slickdaddy') != -1): #my ssh username
			time.sleep(27)                                  #time taken to reach from my desk to coffee machine
			from okcoffeemachine import dispensecoffee

schedule.every().day.at("10:05").do(issession)	#i need a coffee in the morning
schedule.every().day.at("16:30").do(issession)	#i need a coffee in the evening
while True: 
	schedule.run_pending() 
	time.sleep(1) 