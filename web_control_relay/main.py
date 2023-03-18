from microdot_asyncio import Microdot, Response, send_file, redirect
from microdot_utemplate import render_template
from pin_module import PinModule

Response.default_content_type = 'text/html'
app = Microdot()

led = PinModule()
light = PinModule(23)
relay = PinModule(33)

@app.route('/')
async def index(request):
    return render_template('index.html', led_value=led.get_value(), light_value=light.get_value(), relay_value=relay.get_value())

@app.route('toggle_led')
async def toggle_light(self):
    led.toggle()
    return 'OK'

@app.route('toggle_light')
async def toggle_light(self):
    light.toggle()
    return 'OK'

@app.route('toggle_relay')
async def toggle_relay(request):
    relay.toggle()
    return 'OK'

@app.route('static/<path:path>')
def static(request, path):
    return send_file('static/' + path)


app.run(port=80)