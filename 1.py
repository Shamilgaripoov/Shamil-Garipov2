class Batary():
    def __init__(self):
        self.capacity = []
        self.max_charge = 5

    def __str__(self):
        return f'[{"".join(self.capacity)}]'

    def charge(self):
        if len(self.capacity) >= 5:
            print('Батарея заряжена')
        else:
            self.capacity.append(')')

    def discharge(self):
        if len(self.capacity) <= 0:
            print('Батарея разряжена')
        else:
            self.capacity.pop(0)

batary1 = Batary()
batary1.charge()
batary1.charge()
batary1.charge()
batary1.charge()
batary1.charge()
batary1.charge()
print(batary1)

