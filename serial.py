"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        self.start = start
        self.next_serial = start

    def generate(self):
        result = self.next_serial
        self.next_serial += 1 ###this variable is sets up the next serial for when it gets called again
        return result

    def reset(self):
        self.next_serial = self.start

serial = SerialGenerator(start=100)
print(serial.generate())  # prints 100
print(serial.generate())  # prints 101
print(serial.generate())  # prints 102
serial.reset()
print(serial.generate())  # prints 100





