from pump import Pump
from cooler import Cooler
import utils


class PID:
    def __init__(self, P, I, D, NO_errors, TEMPERATURE_FILE_NAME, OD_FILE_NAME):
        self.P = P
        self.I = I
        self.D = D
        self.pump = Pump(33, 27, True)
        self.cooler = Cooler(14)
        self.NO_errors = NO_errors
        self.TEMPERATURE_FILE_NAME = TEMPERATURE_FILE_NAME
        self.OD_FILE_NAME = OD_FILE_NAME
        self.errors = []

    def update(self, temp):
        error = temp - 19
        if len(self.errors) > self.NO_errors:
            self.errors.pop(0)
            self.errors.append(error)
        else:
            self.errors.append(error)

        if len(self.errors) >= 2:
            u_t = error * self.P + self.D * \
                (self.errors[-1] + self.errors[-2]) + self.I * sum(self.errors)
        else:
            u_t = error * self.P + self.I*sum(self.errors)

        utils.saveData(temp, self.TEMPERATURE_FILE_NAME)

        if u_t <= 0.5:
            self.cooler.min()
            self.pump.pump.freq(300)
        elif u_t > 0.5 and u_t <= 6:
            self.cooler.max()
            self.pump.pump.freq(int(15000/6*u_t))
        else:
            self.cooler.max()
            self.pump.pump.freq(15000)
