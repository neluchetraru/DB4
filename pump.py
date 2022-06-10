import machine


class Pump:
    def __init__(self, step, direction):
        self.pump_direction = machine.Pin(direction)
        self.pump_direction.value(1)
        self.pump_step = machine.Pin(step)

    def stepChange(self):
        self.pump_step.value(not self.pump_step.value())
