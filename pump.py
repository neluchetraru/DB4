from machine import PWM, Pin
import utime


class Pump:
    def __init__(self, step, pwm):
        self.pwm = pwm
        if not pwm:
            self.pump = Pin(step, Pin.OUT)
        else:
            self.pump = PWM(Pin(step))
            self.pump.freq(5000)

    def stepChange(self):
        if not self.pwm:
            self.pump.value(1 if self.pump.value() == 0 else 0)
        else:
            pass

    def maxSpeed(self):
        if self.pwm:
            self.pump.freq(13000)
        else:
            while True:
                self.stepChange()
                utime.sleep(5)  # TODO: check later

    def minSpeed(self):
        if self.pwm:
            self.pump.freq(100)
        else:
            pass

    def halfSpeed(self):
        if self.pwm:
            self.pump.freq(6500)
        else:
            pass
