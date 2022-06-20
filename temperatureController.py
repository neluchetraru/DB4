from systemConstants import PIDControl, display, PDSensor, TEMPERATURE_FILE_NAME, mqtt
from read_temp import read_temp, init_temp_sensor
import utils


def handleTemperature():
    temp_sens = init_temp_sensor()
    temp = read_temp(temp_sens)
    PIDControl.update(temp)
    utils.saveData(temp, TEMPERATURE_FILE_NAME)
    mqtt.publish('temperature', temp)
    display.displayTemp(temp)
    print("System temperature -> " + str(temp))
    PDSensor.defaultSettings()
