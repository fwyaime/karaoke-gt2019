import asyncio
import websockets
import time
from gpiozero import LineSensor
from signal import pause

prev_time = 0
time_detected = 0
rpm = 0

def line_detected(websocket, path):
    global prev_time, time_detected, rpm
    prev_time = time_detected
    time_detected = time.time()
    delta_sec = time_detected - prev_time
    rpm = 60 / delta_sec
    print(rpm)
    
async def callback(websocket, path):
    print("Hello")
    
    pause()

start_server = websockets.serve(callback, 'localhost', 4845)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()