"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = ""

    def draw(self):
        print ("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print (f'{self.title} пишет')

class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print (f'{self.title} рисует')

class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print (f'{self.title} выделяет текст')

pen1 = Pen
pencil1 = Pencil
handle1 = Handle

pen1.draw(pen1)
pencil1.draw(pencil1)
handle1.draw(handle1)
