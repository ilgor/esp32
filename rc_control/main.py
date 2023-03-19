from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
import time
from car import Car

app = Microdot()
Response.default_content_type = 'text/html'

car = Car(2, 18, 19, 21)

@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/forward')
async def forward(request):
    car.move_forward()
    return 'OK'

@app.route('/stop')
async def backward(request):
    car.stop()
    return 'OK'

@app.route('/backward')
async def backward(request):
    car.move_backward()
    return 'OK'

@app.route('/left')
async def left(request):
    car.turn_left()
    return 'OK'

@app.route('/right')
async def right(request):
    car.turn_right()
    return 'OK'

app.run(port=80)
