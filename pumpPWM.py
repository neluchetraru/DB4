from machine import Pin, PWM


class PumpPWM:
    def __init__(self, step, direction):
        self.pump_direction = Pin(direction, Pin.OUT)
        self.pump_direction.value(1)
        self.pump = PWM(Pin(step))
        self.pump.freq(5000)

    def maxSpeed(self):
        self.pump.freq(13000)

    def minSpeed(self):
        self.pump.freq(100)

    def halfSpeed(self):
        self.pump.freq(6500)
