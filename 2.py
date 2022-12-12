from abc import ABC, abstractmethod

class Cloth(ABC):

    def __init__(self, V):
        self.V = V

    @abstractmethod
    def reserve(self):
        pass

    def __str__(self):
        return str(self.V)


class Coat(Cloth):
    reserved = 0

    @property
    def reserve(self):
        return self.V / 6.5 + 0.5

class Suit(Cloth):
    reserved = 0

    @property
    def reserve(self):
        return self.V * 2 + 0.3



x1 = Coat(42)
x2 = Suit(165)
print(x1)
print(x1.reserve)
print(x2.reserve)
