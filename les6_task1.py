"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time

class TrafficLight:
    _color = 0

    def running(on_off = False, count = 10):
        print (f'on_off: {on_off}, count= {count}')
        count_int = 0
        TrafficLight._color = 0
        if on_off:
            while count_int < count:
                if TrafficLight._color == 0: # red
                    print ("RED")
                    time.sleep(7)
                if TrafficLight._color == 1: # yellow
                    print ("YELLOW")
                    time.sleep(2)
                if TrafficLight._color == 2: # green
                    print ("GREEN")
                    time.sleep(10)
                    count_int += 1
                TrafficLight._color += 1
                if TrafficLight._color % 3 == 0:
                    TrafficLight._color = 0

svetofor1 = TrafficLight

svetofor1.running(True, 5)
print ("*"*15)
svetofor1.running(True)

