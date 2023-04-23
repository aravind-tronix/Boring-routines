#!/usr/bin/python3

#Author : Aravind
# platform tested : windows and linux
# Python 3.2+
# Created on 08/01/2022
# Deal with my wife please

from telethon import TelegramClient, sync
from random import randrange
from datetime import datetime
import schedule
import time
import os


def sendmessage():
    my_lie_list = [
        "Chellam na vara late aagum, intha manager vaela soli kolran. Saaptu thongu d.",
        "{your wife name} ma, mukiyamana project work iruku d. Vara late aagum. miss u d",
        "Ammu office la unexpected meeting vachitanga. na vara late aagum. saaptu thoongu. lub u d",
        "Baby office la team dinner iruku. Na vara late aagum d."
    ]  # Im not married and Jeni is name of my college crush

    api_id = xxxxxx  # Your telegram api id
    api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Your telegram hash
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    destination_user_username = 'aravind_at_telegram'  # Username of receiver
    entity = client.get_entity(destination_user_username)
    client.send_message(entity=entity, message=my_lie_list[randrange(4)])


def issession():
    # gets only the active sessions
    ActiveConnections = os.popen('last -a | grep -i still').read()
    if (ActiveConnections.find('pi') != -1):  # my ssh username
        sendmessage()


schedule.every().day.at("21:00").do(issession)  # runs at 9:00 PM
while True:
    schedule.run_pending()
    time.sleep(1)
