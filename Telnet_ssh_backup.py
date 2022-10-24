#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:57:11 2022

@author: mobolaji
"""

import netmiko
import getpass
from netmiko import ConnectHandler

connectioninfo = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username" : "cisco",
    "password": "cisco",
    "secret": "class"
}

print("Device Menu")
connectioninfo['username'] = input("Input Device username: ")
connectioninfo['password'] = getpass.getpass("Device password: ")
connectioninfo['secret'] = getpass.getpass("Device Secret: ")
choice = input("ssh (1) or Telnet (2): ")

if choice == "1":
    connectioninfo["device_type"] = "cisco_ios"
    session = netmiko.ConnectHandler(**connectioninfo)
    session.enable()
    output = session.send_command("show running-config")
    print(output)
    choicebckup = input('Do you wnat to create a backup? (Y/N)')
    if choicebckup == 'Y':
        configFile = open("config.txt", "w")
        configFile.write(output)
        configFile.close()
    elif choicebckup == 'N':
        print('No backup created')
    
elif choice == "2":
    connectioninfo["device_type"] = "cisco_ios_telnet"
    session = netmiko.ConnectHandler(**connectioninfo)
    session.enable()
    print(session.send_command("show running-config"))
    
    

else:
    print("Menu Unavailable")
    exit()

