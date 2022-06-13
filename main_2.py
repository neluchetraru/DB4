import machine
import os
import time
from read_temp import read_temp
from cooler import Cooler
from pump import Pump

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
ut_file_name = "ut #.txt"

outputVersion = 1
files = os.listdir()
files.sort()


for file in files[::-1]:
    if file.startswith('temp'):
        try:
            outputVersion = int(file.split()[1].split('.')[0]) + 1
        except:
            pass


temp_file_name = temp_file_name.replace("#", str(outputVersion))
ut_file_name = ut_file_name.replace("#", str(outputVersion))

print(temp_file_name)
open(temp_file_name, 'w')
open(ut_file_name, 'w')


size = 10
while True:
    if time.ticks_diff(time.ticks_ms(), start_time) >= 5000:
        counter -= 5
        start_time = time.ticks_ms()
        temp = read_temp()
        error = 19 - temp
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

        print(temp)
        with open(temp_file_name, 'a') as f:
            f.write("{},{}".format(str(temp), str(u_t)))
            f.close()

        # with open(ut_file_name, 'a') as f:
        #     f.write(str(u_t) + "\n")
        #     f.close()

        if temp <= 19.5:
            cooler.min()
        else:
            cooler.max()

        if u_t < 0:
            temporary = 15000/abs(min(u_ts))
            print(temporary*abs(u_t))
            if temporary*abs(u_t) <= 15000:
                pump2.pump.freq(int(temporary*abs(u_t)))
            else:
                pump2.pump.freq(15000)
        else:
            pump2.pump.freq(0)
        print(u_t)

    if counter == 0:
        break
