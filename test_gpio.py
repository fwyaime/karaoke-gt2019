import time
from gpiozero import LineSensor
from signal import pause

class Reader:
    time_detected = 0.0
    prev_time = 0.0
    
    def line_detected(self):
        self.prev_time = self.time_detected
        self.time_detected = time.time()
        delta_sec = self.time_detected - self.prev_time
        rpm = 60 / delta_sec
        print("RPM %s", rpm)

    def main(self):
        sensor = LineSensor(14, queue_len = 1)
        sensor.when_line = lambda: self.line_detected()
        sensor.when_no_line = lambda: print('No line detected')
        pause()

Reader().main()
