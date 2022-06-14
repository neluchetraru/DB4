import machine
import os
import time
from read_temp import read_temp
from pump import Pump
from MQTT import MQTT
import utils
from pid import PID


TEMPERATURE_FILE_NAME = utils.getNewFileName("temperature")
OD_FILE_NAME = utils.getNewFileName("OD")

pump_algae = Pump(15, 12, False)
PIDControl = PID(2, 0.15, 0, 10, TEMPERATURE_FILE_NAME, OD_FILE_NAME)

start_time = time.ticks_ms()

counter = 15*60*60

# Web server
# mqtt = MQTT()
# mqtt.connectWIFI()
# mqtt.connectMQTT()


while True:
    if time.ticks_diff(time.ticks_ms(), start_time) >= 5000*4*60:
        start_time = time.ticks_ms()
        temp = read_temp()
        PIDControl.update(temp)
        counter -= 5
        print(temp)

    if counter == 0:
        break
