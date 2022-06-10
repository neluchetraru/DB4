import machine
import os
import _thread
import time
from pumpPWM import PumpPWM
from read_temp import read_temp, init_temp_sensor
from cooler import Cooler
from pump import Pump


pump1 = Pump(15, 12)
pump2 = PumpPWM(33, 27)
cooler = Cooler(14)


temps = []
errors = []


temp = read_temp()
start_time = time.ticks_ms()

pump2.maxSpeed()
cooler.max()

counter = 60*60*60

flag = False

Pgain = 2
Dgain = 0.2
Igain = 0.5

u_ts = []


temp_file_name = "temp #.txt"
ut_file_name = "ut #.txt"

outputVersion = 1
files = os.listdir()
for file in files:
    if file.startswith('temp'):
        try:
            outputVersion = int(file.split()[1].split('.')[0]) + 1
        except:
            pass

temp_file_name = temp_file_name.replace("#", str(outputVersion))
ut_file_name = ut_file_name.replace("#", str(outputVersion))

open(temp_file_name, 'w')
open(ut_file_name, 'w')


size = 60
while True:
    if time.ticks_diff(time.ticks_ms(), start_time) >= 5000:
        start_time = time.ticks_ms()
        temp = read_temp()
        if abs(temp-19) <= 1.5:
            flag = True
        if flag:
            error = 19 - temp
            if len(errors) > size:
                errors.pop(0)
                errors.append(error)
                temps.pop(0)
                temps.append(temp)
            else:
                errors.append(error)
                temps.append(temp)

            with open(temp_file_name, 'a') as f:
                f.write(str(temp) + "\n")
                f.close()
            counter -= 5
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
            with open(ut_file_name, 'a') as f:
                f.write(str(u_ts) + "\n")
                f.close()

            if u_t < 0:
                cooler.max()
                if 5000*abs(u_t) <= 15000:
                    pump2.pump.freq(int(5000*abs(u_t)))
                else:
                    pump2.pump.freq(15000)

                print(pump2.pump.freq())
            elif u_t >= 0:
                cooler.min()
        print(temp)
        # try:
        #     times.append(times[-1] + 5)
        # except:
        #     times.append(0)

    if counter == 0:
        print(temps)
        print(u_ts)
        break


# print(temp)
# while True:
#     if temp > 18:
#         cooler.value(0)
#     else:
#         cooler.value(1)
#     time.sleep(1)
