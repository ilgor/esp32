with open('wifi_login.txt', 'r') as f:
    ssid = f.readline().strip()
    password = f.readline().strip()

import network
import time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(1)

print('Wifi connection was succesful! ', 'IP address: ', wifi.ifconfig()[0])