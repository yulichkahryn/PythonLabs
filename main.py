from lab9.device import OperationEnforcer, CurrentSource, VoltageSource, BinaryDemicalDecoder, BinarySummator

obj1 = OperationEnforcer("operation enforcer", 1000, 10, 1800)
obj2 = CurrentSource("current source", 249.99, 500, 10)
obj3 = VoltageSource("voltage source", 260, 400, 8)
obj4 = BinaryDemicalDecoder("binary demical decoder", 340, 5, 10)
obj5 = BinarySummator("binary summator", 549.5, 20, 8)


def print_objects():
    obj1.print_obj()
    obj2.print_obj()
    obj3.print_obj()
    obj4.print_obj()
    obj5.print_obj()


def main():
    print_objects()


if __name__ == '__main__':
    main()
