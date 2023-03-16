import time
import network
from wifi_creds import ssid, password


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(1)

print('Wifi connection was succesful!', 'IP address:', wifi.ifconfig()[0])