import utils
from pid import PID
from pump import Pump
from PD import PD
from display import Display
from MQTT import MQTT

# global variables
global PDSensor
global temp
global PIDControl

P = 2
I = 0.15
D = 0
NO_errors = 10


TEMPERATURE_FILE_NAME = utils.getNewFileName("temperature")
ABSORBANCE_FILE_NAME = utils.getNewFileName("absorbance")
PIDControl = PID(P, I, D, NO_errors, TEMPERATURE_FILE_NAME,
                 ABSORBANCE_FILE_NAME)
PUMP_ALGAE = Pump(15, False)
PDSensor = PD(21, 34)
display = Display()


# web server
mqtt = MQTT()
mqtt.connect()
