import machine


class PinModule:
    def __init__(self, pin_number=2):
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
    
    def get_value(self):
        return self.pin.value()

    def toggle(self):
        self.pin.value(not self.get_value())