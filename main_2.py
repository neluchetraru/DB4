import machine
import os
import utime
import time
from read_temp import read_temp, init_temp_sensor
from pump import Pump
from MQTT import MQTT
import utils
from pid import PID
import _thread
import machine
import ssd1306


TEMPERATURE_FILE_NAME = utils.getNewFileName("temperature")
OD_FILE_NAME = utils.getNewFileName("OD")

# pump_algae = Pump(15, False)

global PIDControl
PIDControl = PID(2, 0.15, 0, 10, TEMPERATURE_FILE_NAME, OD_FILE_NAME)

start_time = time.ticks_ms()

counter = 20*60

# Web server
# mqtt = MQTT()
# mqtt.connectWIFI()
# mqtt.connectMQTT()

# LED = machine.Pin(21, machine.Pin.OUT)
# LED.value(1)

# pd = machine.ADC(machine.Pin(34))
# pd.atten(machine.ADC.ATTN_6DB)
# pd.width(machine.ADC.WIDTH_12BIT)


global temp


time_temp = time.ticks_ms()
time_pd = time.ticks_ms()

i2c = machine.I2C(sda=machine.Pin(23), scl=machine.Pin(22), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# mqtt.subscribeTemp(PIDControl)

while True:
    if time.ticks_diff(time.ticks_ms(), time_temp) >= 5000:  # CHANGEEEEEEEEEEEEEEEEEEEE
        temp_sens = init_temp_sensor()
        temp = read_temp(temp_sens)
        # mqtt.publish('temperature', temp)
        PIDControl.update(temp)
        time_temp = time.ticks_ms()
        # mqtt.client.check_msg()
        utils.TempDisplay(oled, temp)
        # print("Desired temperature -> " + str(PIDControl.desired_temp))
        print("Actual temperature -> " + str(temp))
        # pd.atten(machine.ADC.ATTN_6DB)
        # pd.width(machine.ADC.WIDTH_12BIT)
    # if time.ticks_diff(time.ticks_ms(), time_pd) >= 2000:
    #     value = pd.read()
    #     # mqtt.publish('algaeConcentration', value)
    #     print(value)
    #     time_pd = time.ticks_ms()
    #     utils.ODdisplay(oled, value)
    #     utils.saveData(value, OD_FILE_NAME)
    #     print(PIDControl.test)
