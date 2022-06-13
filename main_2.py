import machine
import os
import time
from read_temp import read_temp
from cooler import Cooler
from pump import Pump
import random
from MQTT import MQTT

pump1 = Pump(15, 12, False)
pump2 = Pump(33, 27, True)
cooler = Cooler(14)


temps = []
errors = []


temp = read_temp()
start_time = time.ticks_ms()

pump2.maxSpeed()
cooler.max()

counter = 10*60

Pgain = 2
Dgain = 0
Igain = 0.5

u_ts = []


temp_file_name = "temp #.txt"
# ut_file_name = "ut #.txt"

temp_file_name = temp_file_name.replace("#", str(random.randint(0, 245887732)))
# ut_file_name = ut_file_name.replace("#", str(outputVersion))

print(temp_file_name)
with open(temp_file_name, 'w') as f:
    f.close()

# open(ut_file_name, 'w')


# Web server
mqtt = MQTT()
mqtt.connectWIFI()
mqtt.connectMQTT()

size = 10

while True:

    # test
    # pump1.stepChange()

    # end test
    if time.ticks_diff(time.ticks_ms(), start_time) >= 5000:
        counter -= 5
        start_time = time.ticks_ms()
        temp = read_temp()
        error = temp - 19
        if len(errors) > size:
            errors.pop(0)
            errors.append(error)
            temps.pop(0)
            temps.append(temp)
        else:
            errors.append(error)
            temps.append(temp)

        if len(errors) >= 2:
            u_t = error * Pgain + Dgain * \
                (errors[-1] + errors[-2]) + Igain * sum(errors)
        else:
            u_t = error * Pgain + Igain*sum(errors)

        if len(errors) > size:
            u_ts.pop(0)
            u_ts.append(u_t)
        else:
            u_ts.append(u_t)

        print("temp: " + str(temp))
        try:
            mqtt.publish('temperature', temp)
        except:
            print('MQTT connection error')
        with open(temp_file_name, 'a') as f:
            f.write(str(temp) + "\n")
            f.close()

        if u_t <= 0.5:
            cooler.min()
            pump2.pump.freq(300)
        elif u_t > 0.5 and u_t <= 6:
            cooler.max()
            pump2.pump.freq(int(15000/6*u_t))
        else:
            cooler.max()
            pump2.pump.freq(15000)

        # if u_t < 0:
        #     temporary = 15000/abs(min(u_ts))
        #     print(temporary*abs(u_t))
        #     if temporary*abs(u_t) <= 15000:
        #         pump2.pump.freq(int(temporary*abs(u_t)))
        #     else:
        #         pump2.pump.freq(15000)
        # else:
        #     pump2.pump.freq(200)
        print("u_t: " + str(u_t))
        print("pump: " + str(pump2.pump.freq()))

    if counter == 0:
        break
