import time
from gpiozero import LineSensor
from signal import pause
import asyncio
import websockets

prev_time = 0
time_detected = 0
rpm = 0
count = 0

def line_detected():
    global prev_time, time_detected, rpm
    prev_time = time_detected
    time_detected = time.time()
    delta_sec = time_detected - prev_time
    rpm = 60 / delta_sec
    print(rpm)

async def test(websocket, path):
    old_rpm = 0
    global rpm, count
    while True:
        if rpm == old_rpm:
            count += 1
        else:
            count = 0
        if count > 3:
            rpm = 0
        else:
            old_rpm = rpm
            now = str(rpm)
            await websocket.send(now)
            time.sleep(1)

start_server = websockets.serve(test, '127.0.0.1', 8080)

sensor = LineSensor(15, queue_len = 1)
sensor.when_line = lambda: line_detected()
sensor.when_no_line = lambda: print('No line detected')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
