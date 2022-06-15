import machine
import os
import utime
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

counter = 1*60

# Web server
# mqtt = MQTT()
# mqtt.connectWIFI()
# mqtt.connectMQTT()

pump_algae = Pump(15, 12, False)


LED = machine.Pin(21, machine.Pin.OUT)
LED.value(1)
OD = "OD #.txt"
ver = 1
for file in os.listdir():
    if file.startswith("OD"):
        ver += 1

OD = OD.replace("#", str(ver))

with open(OD, 'w') as f:
    f.close()


pd = machine.ADC(machine.Pin(36))
pd.atten(machine.ADC.ATTN_11DB)
# pd.width(machine.ADC.WIDTH_12BIT)


pump_start = time.ticks_ms()

while True:
    if time.ticks_diff(time.ticks_ms(), pump_start) < 30000:
        pump_algae.pump.value(1 if pump_algae.pump.value() == 0 else 0)
    else:
        pump_algae.pump.value(1 if pump_algae.pump.value() == 0 else 0)
        time.sleep(0.001)
    if time.ticks_diff(time.ticks_ms(), start_time) >= 5000:
        value = pd.read()
        with open(OD, 'a') as f:
            f.write(str(value) + "\n")
            f.close()
        print(value)
        start_time = time.ticks_ms()
        temp = read_temp()
        PIDControl.update(temp)
        counter -= 5
        print(temp)
    if counter == 0:
        total = 0
        with open(OD, 'r') as f:
            for line in f:
                num = float(line)
                total += num
            f.close()
            with open(OD, 'a') as g:

                g.write(str(total/12) + "\n")
                g.close()
        break
