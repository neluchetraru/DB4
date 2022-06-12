from machine import PWM, Pin
import utime


class Pump:
    def __init__(self, step, direction, PWM):
        self.pump_direction = Pin(direction, Pin.OUT)
        self.pump_direction.value(1)
        self.PWM = PWM
        if not PWM:
            self.pump = Pin(step)
        else:
            self.pump = PWM(Pin(step))
            self.pump.freq(5000)

    def stepChange(self):
        if not self.PWM:
            self.pump.value(not self.pump_step.value())
        else:
            pass

    def maxSpeed(self):
        if self.PWM:
            self.pump.freq(13000)
        else:
            while True:
                self.stepChange()
                utime.sleep(5)  # TODO: check later

    def minSpeed(self):
        if self.PWM:
            self.pump.freq(100)
        else:
            pass

    def halfSpeed(self):
        if self.PWM:
            self.pump.freq(6500)
        else:
            pass
