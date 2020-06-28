"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения
данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить
метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины
полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    _length = 0
    _width = 0
    _weight = 0
    _mass1kvm1sm = 25
    _thickness = 5

    def __init__(self, len_road, width_road, thickness = 5):
        # print (len_road, width_road, thickness)
        self._length = len_road
        self._width = width_road
        self._thickness = thickness

    def print_weight(self):
        print (f'Для дороги длиной {self._length} м, шириной {self._width} м, толщиной {self._thickness} см')
        self._weight = self._width * self._length * self._mass1kvm1sm * self._thickness
        print (f'Масса асфальта составит: {self._weight/1000.0} т ')


road1 = Road(5000, 20, 5)

road1.print_weight()


