import time
from gpiozero import LineSensor
from signal import pause
import asyncio
import websockets

class Reader:
    time_detected = 0.0
    prev_time = 0.0
    
    async def line_detected(self):
        self.prev_time = self.time_detected
        self.time_detected = time.time()
        delta_sec = self.time_detected - self.prev_time
        rpm = 60 / delta_sec
        print(rpm)
        async with websockets.connect('ws://localhost:4845') as websocket:
            await websocket.send(str(rpm))

    def eventhandler(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.line_detected())
            
    def main(self):
        sensor = LineSensor(14)
        sensor.when_line = lambda: self.eventhandler()
        sensor.when_no_line = lambda: print('No line detected')
        pause()

Reader().main()