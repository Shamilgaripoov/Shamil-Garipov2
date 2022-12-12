from random import randint

class Box():
    def __init__(self, postcode, name, from_city, target_city):
        self.__name = name
        self.__postcode = postcode
        self.__from_city = from_city
        self.__target_city = target_city

    def get_postcode(self):
        self.__posctcode = randint(100000, 999999)

    @property
    def posctcode(self):
        return self.__posctcode

    @property
    def name(self):
        return self.__name

    @property
    def from_city(self):
        return self.__from_city

    @property
    def target_city(self):
        return self.__target_city

    @target_city.setter
    def target_city(self, new_target):
        self.__target_city = new_target


x = Box(randint, 'Sham', 'USA', 'Kazan')
print(x.name)
print(x.from_city)
print(x.target_city)
