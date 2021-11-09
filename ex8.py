"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

# class Data:
#
#     @classmethod
#     def extract(cls, date):
#         x = date.split("-")
#         a = []
#         for el in x:
#             a.append(int(el))
#         return a
#
#     @staticmethod
#     def valid(date):
#         day, month, year = date
#         if day not in range(1, 32):
#             print("День указан некорректно")
#             x = True
#         else:
#             x = False
#             if month not in range(1, 13):
#                 print("Месяц указан некорректно")
#                 x = True
#             else:
#                 x = False
#                 if year not in range(1, 3000):
#                     print("Год указан некорректно")
#                     x = True
#                 else:
#                     x = False
#         if x == False:
#             print("Валидация прошла успешно")
#
#
# my_date = Data()
# date_extract = my_date.extract("37-12-2021")
# my_date.valid(date_extract)

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""

# class DivisionByZero(Exception):
#
#     def __init__(self):
#         self.message = "Деление на ноль"
#
#
# def division(devidend, devider):
#     try:
#         if devider == 0:
#             raise DivisionByZero
#         print(devidend / devider)
#     except DivisionByZero as err:
#         print(err.message)
#
# division(1, 0)

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""

# class OnlyInt(Exception):
#     def __init__(self):
#         self.message = "Нужно ввести число"
#
#
# my_list = []
# my_string = input("Введите значение и нажмите Enter. Для остановки введите stop. ")
# while my_string != "stop":
#     try:
#         if my_string.isdigit():
#             my_list.append(int(my_string))
#         else:
#             raise OnlyInt
#     except OnlyInt as err:
#         print(err.message)
#     my_string = input("Введите значение и нажмите Enter. Для остановки введите stop. ")
# print(my_list)

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


# class Store:
#     model_quantity = {}
#
#     @classmethod
#     def store_to(cls, eq_type, eq_model, eq_quantity):
#         cls.model_quantity[eq_type][eq_model]["quantity"] += eq_quantity
#
#     @classmethod
#     def store_from(cls, eq_type, eq_model, eq_quantity):
#         quantity1 = cls.model_quantity[eq_type][eq_model]["quantity"]
#         if quantity1 < eq_quantity:
#             raise ValueError
#         else:
#             cls.model_quantity[eq_type][eq_model]["quantity"] -= eq_quantity
#
#     @staticmethod
#     def all_store():
#         for key, value in Store.model_quantity.items():
#             print(key, value)
#
#
# class Equipment:
#
#     def __init__(self, model, equipment, quantity=0):
#         self.equipment = equipment
#         self.model = model
#         try:
#             if type(quantity) not in [int, float]:
#                 self.__quantity = 0
#                 raise ValueError
#         except ValueError:
#             print("Неверный формат данных")
#         else:
#             self.__quantity = quantity
#         finally:
#             self.update_store()
#
#     def update_store(self):
#         eq_type = Store.model_quantity.get(self.equipment, {})
#         if self.model in eq_type.keys():
#             eq_model = eq_type(self.model)
#             eq_model["quantity"] += self.__quantity
#         else:
#             eq_type[self.model] = {"quantity": self.__quantity}
#
#         Store.model_quantity[self.equipment] = eq_type
#
#
# class Printer(Equipment):
#     def __init__(self, model, quantity, print_type):
#         super().__init__(model, "Printer", quantity)
#         self.print_type = print_type
#
#
# class Notebook(Equipment):
#     def __init__(self, model, quantity, os, ssd, ram):
#         super().__init__(model, "Notebook", quantity)
#         self.os = os
#         self.ssd = ssd
#         self.ram = ram
#
#
# printer_1 = Printer("HP LaserJet Pro M211d", 100, "черно-белая печать")
# printer_2 = Printer("HP Color Laser 150a", 50, "цветная печать")
# notebook_1 = Notebook("Macbook Air 13, 128, 8", 50, "MacOS", 128, 8)
# notebook_2 = Notebook("Macbook Air 13, 256, 8", 50, "MacOS", 256, 8)
# notebook_3 = Notebook("Macbook Air 13, 256, 8", 50, "MacOS", 256, 8)
# notebook_4 = Notebook("Macbook Air 13, 256, 16", 50, "MacOS", 256, 16)
# notebook_5 = Notebook("Macbook Air 13, 512, 16", 50, "MacOS", 512, 16)
# Store.all_store()

"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


# class ComplexNumber:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         return f'Сумма: {ComplexNumber(self.a + other.a, self.b + other.b)}'
#
#     def __mul__(self, other):
#         return f'Произведение: {ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)}'
#
#     def __str__(self):
#         return f'{self.a} + {self.b}j'
# 
#
# complex_number_1 = ComplexNumber(1, -2)
# complex_number_2 = ComplexNumber(3, 4)
# print(complex_number_1 + complex_number_2)
# print(complex_number_1 * complex_number_2)