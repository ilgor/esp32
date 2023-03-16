import machine
import time

green = machine.Pin(18, machine.Pin.OUT)
yellow = machine.Pin(19, machine.Pin.OUT)
red = machine.Pin(21, machine.Pin.OUT)
relay = machine.Pin(15, machine.Pin.OUT)

lights = ['green', 'yellow', 'red']

for light in lights:
    if light == 'green':
        green.on()
        relay.on()
    elif light == 'yellow':
        yellow.on()
    elif light == 'red':
        red.on()
        relay.off()
    print(light)
    time.sleep(.5)
    red.off()
    yellow.off()
    green.off()
    time.sleep(.5)
print("done!")

