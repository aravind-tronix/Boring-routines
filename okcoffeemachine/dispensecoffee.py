#!/usr/bin/python

#Author : Aravind
#platform tested : windows and linux
#Python 3.2+
#Created on 08/01/2022
#MQTT publish 

import paho.mqtt.client as paho
import json
 
connflag = False

connected = json.dumps({"status":True})
disconnected = json.dumps({"status":False})
dispensecoffee = json.dumps({"brew":"coffee"})
 
def on_connect(client, userdata, flags, rc):                # func for making connection
	global connflag
	connflag = True
	mqttc.publish("connectivity",payload=connected, qos=0, retain=False)
	mqttc.publish("coffee",payload=dispensecoffee, qos=0, retain=False)

 
def on_message(client, userdata, msg):                      # Func for Sending msg
	print(msg.topic+" "+str(msg.payload))
 
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters #### 
awshost = "localhost"     # Endpoint
awsport = 1883            # Port no.   
 
mqttc.will_set("connectivity",payload=disconnected, qos=0, retain=False)
mqttc.connect(awshost, awsport, keepalive=60)