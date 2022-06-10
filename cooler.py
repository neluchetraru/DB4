from machine import Pin


class Cooler:
    def __init__(self, pin):
        self.cooler = Pin(pin, Pin.OUT)
        self.cooler.value(1)

    def max(self):
        self.cooler.value(0)

    def min(self):
        self.cooler.value(1)
