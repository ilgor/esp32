import machine
from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template

led_pin = machine.Pin(2, machine.Pin.OUT)
app = Microdot()
Response.default_content_type = 'text/html'

@app.get('/')
async def index(request):
    return render_template("index.html")

@app.route('on')
async def on(request):
    led_pin.on()
    return 'LED is ON'

@app.route('off')
async def off(request):
    led_pin.off()
    return 'LED is OFF'

@app.route("/static/<path:path>")
def static(request, path):
    print(path)
    if ".." in path:
        return "Not found", 404
    return send_file("static/" + path)

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()
        
start_server()
