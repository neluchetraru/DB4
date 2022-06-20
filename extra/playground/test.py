from time import time
from machine import Pin, Timer
import micropython
import utime

red = Pin(27, Pin.OUT)  # temperature
orange = Pin(33, Pin.OUT)  # concentration
green = Pin(15, Pin.OUT)  # pump_algae

timer0 = Timer(0)  # Timer handleTemperature
timer1 = Timer(1)  # Timer handleConcentration
timer2 = Timer(2)  # Timer pump_algae


def toggleLed(led):
    led.value(not led.value())


def cb2(t):
    greenStart = utime.ticks_ms()
    while True:
        toggleLed(green)
        utime.sleep_ms(500)
        if utime.ticks_diff(utime.ticks_ms(), greenStart) > 5000:
            start()
            break


def cb1(t):
    toggleLed(orange)
    timer0.init(mode=Timer.ONE_SHOT, callback=cb0, period=500)
    if utime.ticks_diff(utime.ticks_ms(), timeStart) > 10000:
        timer2.init(mode=Timer.ONE_SHOT, callback=cb2, period=0)


def cb0(t):
    timer1.init(mode=Timer.ONE_SHOT, callback=cb1, period=500)
    toggleLed(red)


def start():
    global timeStart
    timeStart = utime.ticks_ms()
    timer0.init(mode=Timer.ONE_SHOT, callback=cb0, period=0)


def _cb0(t):
    toggleLed(red)


def _cb1(t):
    toggleLed(green)


def _cb2(t):
    startTime = utime.ticks_ms()
    while True:
        if utime.ticks_diff(utime.ticks_ms(), startTime) > 5000:
            break
        toggleLed(orange)
        utime.sleep_ms(1000)


def test0():
    timer0.init(mode=Timer.PERIODIC, callback=_cb0, period=200)
    timer1.init(mode=Timer.PERIODIC, callback=_cb1, period=600)
    timer2.init(mode=Timer.PERIODIC, callback=_cb2, period=10000)
