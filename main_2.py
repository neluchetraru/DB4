from pump import Pump
import time
from systemConstants import PIDControl, mqtt, PDSensor
from concentrationController import handleConcentration, getConcentration
from temperatureController import handleTemperature
from machine import Timer
import _thread
import utime


running = True
PUMP_ALGAE = Pump(15, True)


class System:
    def __init__(self):
        self.running = True

    def cb(self, topic, message):
        topic = topic.decode('utf-8').split('/')[2]
        global running

        if topic == "startsystem":
            if str(message, 'utf-8') == 'ON':
                running = True
            else:
                PUMP_ALGAE.minSpeed()
                PIDControl.pump.minSpeed()
                running = False
        elif topic == "desiredtemp":
            print('test topic')
            temp = int(message.decode('utf-8'))
            PIDControl.updateTemp(temp)

    def thread(self):
        while True:
            if running:
                handleTemperature()
                time.sleep(7.5)
                handleConcentration()
                time.sleep(7.5)
            else:
                time.sleep(10)

    def thread1(self):
        while True:
            if mqtt.online:
                mqtt.client.check_msg()
                time.sleep(1)

    def feedingControl(self):
        startFeed = utime.ticks_ms()
        while True:
            total = 0
            for i in range(15):
                total += getConcentration(PDSensor.getAbsorbance())
            algae_concentration = total/15

            volume_needed = (4000*937.5) / algae_concentration
            time_needed = volume_needed / 0.605
            if utime.ticks_diff(utime.ticks_ms(), startFeed) < time_needed * 1000:
                PUMP_ALGAE.pump.freq(9000)
            else:
                PUMP_ALGAE.pump.freq(100)
                time.sleep(5*60)  # 5 minutes
                startFeed = utime.ticks_ms()

    def start(self):
        if mqtt.online:
            mqtt.subscribeData(self.cb, 'desiredtemp')
            mqtt.subscribeData(self.cb, 'startsystem')
        _thread.start_new_thread(self.feedingControl, ())
        _thread.start_new_thread(self.thread, ())
        _thread.start_new_thread(self.thread1, ())


sys = System()
sys.start()
