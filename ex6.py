"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

# from time import sleep
# from itertools import cycle
#
#
# class TrafficLight:
#     __colors = ("красный", "желтый", "зеленый")
#     times = (7, 2, 6)
#
#     def running(self):
#         my_cycle = cycle(self.__colors)
#         for i in my_cycle:
#             print(i)
#             sleep(self.times[self.__colors.index(i)])
#
#
# my_traffic = TrafficLight()
# my_traffic.running()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def mass_calc(self):
#         total_mass = self._length * self._width * 25 * 0.5
#         return f'Масса асфальта: {total_mass}'
#
#
# road = Road(20, 5000)
# print(road.mass_calc())

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#
#     def get_total_income(self):
#         return self._income.get("wage") + self._income.get("bonus")
#
#
# my_position = Position("Иван", "Сергеев", "Технический директор", 150000, 100000)
# print(f'{my_position.get_full_name()} получает {my_position.get_total_income()}')

"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


# class Car:
#
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'Автомобиль {self.color} {self.name} поехал'
#
#     def stop(self):
#         return f'Автомобиль {self.color} {self.name} остановился'
#
#     def turn(self, direction):
#         return f'Автомобиль {self.color} {self.name} повернул {direction}'
#
#     def current_speed(self):
#         print(f'Текущая скорость автомобиля: {self.speed}')
#
# class TownCar(Car):
#
#     def current_speed(self):
#         if self.speed > 60:
#             print("Превышение скорости!")
#         else:
#             Car.current_speed(self)
#
# class WorkCar(Car):
#
#     def current_speed(self):
#         if self.speed > 40:
#             print("Превышение скорости!")
#         else:
#             Car.current_speed(self)
#
# class PoliceCar(Car):
#
#     def go(self):
#         return f'Полицейский автомобиль {self.color} {self.name} поехал'
#
#     def stop(self):
#         return f'Полицейский автомобиль {self.color} {self.name} остановился'
#
#
# my_town_car = TownCar(50, "белый", "BMW", False)
# print(my_town_car.go())
# print(my_town_car.turn("налево"))
# print(my_town_car.stop())
# my_town_car.current_speed()
#
# my_work_car = WorkCar(50, "черный", "Audi", False)
# print(my_work_car.go())
# my_work_car.current_speed()
# print(my_work_car.stop())
#
# my_police_car = PoliceCar(40, "синий", "Ford", True)
# print(my_police_car.go())
# print(my_police_car.turn("направо"))
# print(my_police_car.stop())
# my_police_car.current_speed()

"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


# class Stationery:
#
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print("Запуск отрисовки.")
#
#
# class Pen(Stationery):
#
#     def draw(self):
#         super().draw()
#         print(f"Будет использована {self.title}.")
#
#
# class Pencil(Stationery):
#     def draw(self):
#         super().draw()
#         print(f"Будет использован {self.title}.")
#
#
# class Handle(Stationery):
#     def draw(self):
#         super().draw()
#         print(f"Будет использован {self.title}.")
#
#
# my_pen = Pen("ручка")
# my_pen.draw()
# my_pencil = Pencil("карандаш")
# my_pencil.draw()
# my_handle = Handle("маркер")
# my_handle.draw()

