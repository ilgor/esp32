import time
import network
from wifi_creds import ssid, password
 
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(ssid, password)
    
    while not sta_if.isconnected():
        time.sleep(1)
print('network config:', sta_if.ifconfig())