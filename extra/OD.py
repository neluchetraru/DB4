import time
import machine
import os 

#Photodiode

LED = machine.Pin(33,machine.Pin.OUT)
LED.value(1)


pd = machine.ADC(machine.Pin(36))
pd.atten(machine.ADC.ATTN_6DB)
pd.width(machine.ADC.WIDTH_12BIT)


#for the file
OD = "OD #.txt"
ver = 1
for file in os.listdir():
    if file.startswith("OD"):
        ver += 1 

OD = OD.replace("#", str(ver))

with open(OD, 'w') as f:
    f.close()
counter =60
start_time = time.ticks_ms()
while True:
    if time.ticks_diff(time.ticks_ms(), start_time) >= 5000:
    #time.sleep(1)
        counter -= 5
        start_time = time.ticks_ms()
        
        value = pd.read()
        
        with open(OD, 'a') as f:
            f.write(str(value) + "\n" )
            f.close()
        print(value)

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



