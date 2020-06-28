"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""
class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"salary": 0, "prize": 0}

    def __init__(self, name, surname, position, total_income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = total_income

    def set_income(self, wage, bonus):
        self._income["salary"] = wage
        self._income["prize"] = bonus

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.set_income(wage, bonus)

    # def __init__(self, position):
    #     self.position = position

    def set_full_name(self, name, surname):
        self.name = name
        self.surname = surname

    def set_total_income(self, wage, bonus):
        super().set_income(wage, bonus)

    def get_full_name(self):
        print (f'Name: {self.name}\nSurname: {self.surname}')

    def get_position(self):
        print (f'Position: {self.position}')

    def get_total_income(self):
        print (f'Income: {super()._income["salary"]} (wage); {super()._income["prize"]} (bonus)')


person1 = Position("Mark", "Dartun", "Employee", 1000, 200)

person1.get_full_name()
person1.get_position()
person1.get_total_income()

person2 = Position("Petr", "Tarfet", "Engineer", 1500, 500)

person2.get_full_name()
person2.get_position()
person2.get_total_income()

