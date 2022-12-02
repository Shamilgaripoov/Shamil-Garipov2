class Father():
    def __init__(self):
        self.surname = "Garipov"

class Child(Father):
    pass
Baby = Child()

class Father:
    def __init__(self, name):
        self.name = name

class child(Father):
    def __init__(self, name, patronim):
        super(child, self).__init__(name)
        self.patronim = patronim
Children = child("Shamile","Insafovich")

print(Baby.surname, Children.name, Children.patronim)