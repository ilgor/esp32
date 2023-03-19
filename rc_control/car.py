import machine

class Car:
    def __init__(self, forward=2, backward=2, right=2, left=2) -> None:
        self.forward = machine.Pin(forward, machine.Pin.OUT)
        self.backward = machine.Pin(backward, machine.Pin.OUT)
        self.right = machine.Pin(right, machine.Pin.OUT)
        self.left = machine.Pin(left, machine.Pin.OUT)
    
    def move_forward(self):
        self.forward.on()
    
    def move_backward(self):
        self.backward.on()

    def turn_right(self):
        self.right.on()

    def turn_left(self):
        self.left.on()
    
    def stop(self):
        self.forward.off()
        self.backward.off()
        self.right.off()
        self.left.off()
