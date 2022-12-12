class Person():

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @age.setter
    def age(self, new_age):
        self.__age = new_age


f = Person('Alex', 'Ford', '15')
print(f.name)
print(f.surname)
print(f.age)

f.name = 'Shamile'
f.surname = 'Garipov'
f.age = '18'
print(f.name)
print(f.surname)
print(f.age)
