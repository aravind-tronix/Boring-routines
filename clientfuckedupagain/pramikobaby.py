#Author : Aravind
# platform tested : windows and linux
# Python 3.7+
# Created on 08/01/2022
# ssh client pramiko

import paramiko


def sshconnection():
    host = "xx.xx.xx.xx"  # clients host
    username = "Aravind"  # ssh username
    password = "xxxxx"  # password

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(
        "python3 /home/mongobackup/restoredb.py")  # script to restore the latest db backup
    client.close()
