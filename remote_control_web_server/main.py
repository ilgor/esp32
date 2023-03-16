import machine
from microdot_asyncio import Microdot

led_pin = machine.Pin(2, machine.Pin.OUT)
app = Microdot()

@app.route('/')
async def hello(request):
    return 'Hello world'

@app.route('on')
async def on(request):
    led_pin.on()
    return 'LED is ON'

@app.route('off')
async def on(request):
    led_pin.off()
    return 'LED is OFF'

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()
        
start_server()