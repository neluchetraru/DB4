from systemConstants import PDSensor, display, ABSORBANCE_FILE_NAME, mqtt
import utils


def getConcentration(absorbance):
    return (absorbance - 4081.6) / (-0.0007)


def handleConcentration():
    concentration = getConcentration(PDSensor.getAbsorbance())
    mqtt.publish('algaeConcentration', concentration)
    display.displayConcentration(concentration)
    print("Algae concentration -> ", concentration)
    utils.saveData(concentration, ABSORBANCE_FILE_NAME)
