class Stationery():
    def __init__(self,title):
        self.title = title

    def set_color(self):
        self.set_color = "желтым цветом"
        return self.set_color

    def draw(self):
        pass

class Pen(Stationery):
    def color(self):
        super().__init__(title = "Ручка: ")
        self.color = "желтый"

    def draw(self):
        self.f = "Ручка пишет"
        return self.f

class Pencil(Stationery):
    def draw(self):
        self.f = "Карандащ пишет"
        return self.f

class Handle(Stationery):
    def draw(self):
        self.f = "Маркер пишет"
        return self.f

pen = Pen('ручка:')
pencil = Pencil('карандаш:')
handle = Handle('маркер:')

print(pen.title,pen.draw(), pen.set_color())
print(pencil.title, pencil.draw(), pencil.set_color())
print(handle.title, handle.draw(), handle.set_color())