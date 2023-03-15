import network
import time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.contact('wifi name', 'wifi password')

while not wifi.isconnected():
    time.sleep(1)

print('Wifi connection was succesful! ', 'IP address: ', wifi.ifconfig()[0])