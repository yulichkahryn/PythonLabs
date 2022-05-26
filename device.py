class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}')


class Source(Device):
    def __init__(self, name, price, resistance):
        super().__init__(name, price)
        self.resistance = resistance

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, resistance: {self.resistance}')


class Analogue(Device):
    def __init__(self, name, price, period):
        super().__init__(name, price)
        self.period = period

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, period: {self.period}')


class Digital(Device):
    def __init__(self, name, price, time):
        super().__init__(name, price)
        self.time = time

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, time: {self.time}')


class Impulsive(Device):
    def __init__(self, name, price, impulse):
        super().__init__(name, price)
        self.impulse = impulse

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, impulse: {self.impulse}')


class VoltageSource(Source):
    def __init__(self, name, price, resistance, voltage):
        super().__init__(name, price, resistance)
        self.voltage = voltage

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, resistance: {self.resistance}, voltage: {self.voltage}')


class CurrentSource(Source):
    def __init__(self, name, price, resistance, current):
        super().__init__(name, price, resistance)
        self.current = current

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, resistance: {self.resistance}, current: {self.current}')


class OperationEnforcer(Analogue):
    def __init__(self, name, price, period, power):
        super().__init__(name, price, period)
        self.power = power

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, period: {self.period}, power: {self.power}')


class BinaryDemicalDecoder(Digital):
    def __init__(self, name, price, time, current):
        super().__init__(name, price, time)
        self.current = current

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, time: {self.time}, current: {self.current}')


class BinarySummator(Impulsive):
    def __init__(self, name, price, impulse, voltage):
        super().__init__(name, price, impulse)
        self.voltage = voltage

    def print_obj(self):
        print(f'name: {self.name}, price: {self.price}, impulse: {self.impulse}, voltage: {self.voltage}')

