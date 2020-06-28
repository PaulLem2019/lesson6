"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    speed = 0
    color = "Black"
    name = "Toyota"
    is_police = False
    _move = 0
    status = "городская машина"

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self. is_police = is_police

    def go(self):
        self._move = 1
        print (f"{self.status} {self.name} поехала")

    def set_speed(self, speed):
        if self._move:
            self.speed = speed
        else:
            self.speed = 0

    def stop(self):
        self._move = 0
        print (f"{self.status} {self.name} остановилась")

    def turn(self, direction):
        if direction == "Вперед":
            print (f"{self.status} {self.name} едет прямо")
        elif direction == "Направо":
            print(f"{self.status} {self.name} повернула направо")
        elif direction == "Налево":
            print(f"{self.status} {self.name} повернула налево")
        elif direction == "Назад":
            print (f"{self.status} {self.name} едет назад")
        else:
            print (f"Направление {self.status} {self.name} не определено")

    def show_speed(self):
        print (f"скорость {self.status} {self.name}: {self.speed}")

class TownCar(Car):
    def __init__(self, name, color, is_police):
        super(TownCar, self).__init__(name, color, is_police)
        self.status = "городская машина"

    def show_speed(self):
        print (f"скорость {self.status} {self.name}: {self.speed}")
        if self.speed > 60:
            print (f"скорость {self.status} {self.name} превышена")

class SportCar(Car):
    def __init__(self, name, color, is_police):
        super(SportCar, self).__init__(name, color, is_police)
        self.status = "спортивная машина"

class WorkCar(Car):
    def __init__(self, name, color, is_police):
        super(WorkCar, self).__init__(name, color, is_police)
        self.status = "рабочая машина"

    def show_speed(self):
        print(f"скорость машины {self.name}: {self.speed}")
        if self.speed > 40:
            print (f"скорость {self.status} {self.name} превышена")

class PoliceCar(Car):
    def __init__(self, name, color, is_police):
        super(PoliceCar, self).__init__(name, color, is_police)
        self.status = "полицейская машина"


sport_car = SportCar("Bugatti", "red", False)
town_car = TownCar("Nissan", "greay", False)
work_car = WorkCar("Renault", "white", False)
police_car = PoliceCar("Lada", "Gray", True)

sport_car.go()
town_car.go()
work_car.go()
police_car.go()

sport_car.set_speed(90)
town_car.set_speed(80)
work_car.set_speed(70)
police_car.set_speed(60)

sport_car.turn("Вперед")
town_car.turn("Влево")
work_car.turn("Назад")
police_car.turn("Вправо")

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()

sport_car.stop()
town_car.stop()
work_car.stop()
police_car.stop()
