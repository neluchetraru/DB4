import ssd1306
import machine


class Display:
    def __init__(self):
        i2c = machine.I2C(sda=machine.Pin(
            23), scl=machine.Pin(22), freq=100000)
        self.display = ssd1306.SSD1306_I2C(128, 32, i2c)

    def displayTemp(self, temp):
        self.display.fill(0)
        self.display.text("Temperature: ", 0, 8)
        self.display.text(str(temp), 10, 17)
        self.display.show()

    def displayConcentration(self, concentration):
        self.display.fill(0)
        self.display.text("Concentration: ", 0, 8)
        self.display.text(str(concentration), 10, 17)
        self.display.show()
