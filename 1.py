class animal():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

class Cat(animal):
    def __init__(self, say):
        super().__init__('Pesik', 'gold', 3)
        self.say = say

class Doggy(animal):
    def __init__(self, say):
        super().__init__('mike', 'brown', 1)
        self.say = say

Animal_cat = Cat('myayyyy')
Animal_dog = Doggy('gav')
print(Animal_cat.say)
print(Animal_cat.say)
print(Animal_cat.name)
print(Animal_cat.color)
print(Animal_cat.age)
print(Animal_cat.say)

print(Animal_dog.say)
print(Animal_dog.say)
print(Animal_dog.name)
print(Animal_dog.color)
print(Animal_dog.age)
print(Animal_dog.say)
