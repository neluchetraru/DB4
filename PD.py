import machine


class PD:
    def __init__(self, LEDPin, PDPin):
        self.LED = machine.Pin(LEDPin, machine.Pin.OUT)
        self.LED.value(1)
        self.pd = machine.ADC(machine.Pin(PDPin))
        self.pd.atten(machine.ADC.ATTN_11DB)
        self.pd.width(machine.ADC.WIDTH_12BIT)

    def defaultSettings(self):
        self.pd.atten(machine.ADC.ATTN_11DB)
        self.pd.width(machine.ADC.WIDTH_12BIT)

    def getAbsorbance(self):
        return self.pd.read()
