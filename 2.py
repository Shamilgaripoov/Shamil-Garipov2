class Queue():
    def __Init__(self):
        self.inside = []

    def __add__(self, other):
        self.inside.append(other)

    def __sub__(self, other):
        self.inside.pop(other)

    def __iadd__(self, other):
        self.inside.append(other)
        return self

    def __isub__(self, other):
        self.inside.pop(other)
        return self

    def __str__(self):
        return f'[{"".join(self.inside)}]'

    def add(self):
        name = input('Имя: ')
        self.inside.append(name)

    def take_out(self):
        self.inside.pop(0)

    def name(self):
        name = input('Имя: ')
        return name

que1 = Queue()
que1.add()
que1.take_out()
que1.name()
print(que1)

