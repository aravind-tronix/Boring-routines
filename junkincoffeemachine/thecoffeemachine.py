#Author : Aravind
#platform tested : Raspbian(linux based operating system)
#Python 3.2+
#Created on 08/01/2022
#MQTT protocol for less latency/power consuption 

import paho.mqtt.client as paho
from time import sleep
import json
import RPi.GPIO as GPIO
import time

MOTOR_PIN = 17 #hardware pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)



def on_connect(client, userdata, flags, rc):                # func for making connection
	client.subscribe("coffee" , 0 )
	global connflag
	connflag = True
 
def on_message(client, userdata, msg):                      # Func for receiving msgs
	print(msg.topic)
	if msg.topic == "coffee":
		global topic
		rtopic=((msg.payload))
		payload = json.loads(rtopic)
		if payload["brew"] == "coffee":
			GPIO.output(MOTOR_PIN, GPIO.HIGH)
			time.sleep(7)                                   #exact time to fill a cup of coffee
			GPIO.output(MOTOR_PIN, GPIO.LOW)
			GPIO.cleanup()

mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters ####  
awshost = "localhost"     # Endpoint
awsport = 1883            # Port no.   
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_forever()  