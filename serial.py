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
    def __init__(self, start, num = None):
        self.start = start - 1
        self.num = self.start


    def generate(self):
        self.start +=  1
        return (self.start)

    def reset(self):
        self.start = self.num
        return ''
        
   
        

serial = SerialGenerator(100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
