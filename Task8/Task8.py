# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
err_log_path = r"C:\Users\sergei.novikov\Desktop\Study\BasicGit\basics_py\Task8\err_log.txt"


class LenError(Exception):
    def __init__(self):
        self.txt = "Array length doesn't match"


class DateError(Exception):
    def __init__(self):
        self.txt = "Error in date"


class Date:

    def __init__(self, date: str):
        self.date = date

    @property  # решил через проперти, чтобы дата записанная в нужном формате хранилась в классе как поле
    def extract_number(self) -> list:
        date = self.date.split("-")
        result = []
        try:
            if len(date) > 3:
                raise LenError
            for element in date:
                element = int(element)  # строка 24 отработает ошибку, если элемент не число
                result.append(element)
        except LenError as err_format:  # Ловим ошибку в длине массива, т.к маска даты dd-mm-yyyy
            print("Error! Incorrect format of date. Must be: dd-mm-yyyy")
            with open(err_log_path, "a") as err_log:
                print(err_format, file=err_log)
            return []
        except ValueError as err_letters:  # Ловим ошибку при переводе буквы в число, строка 27
            print("Error! Date exists the letters")
            with open(err_log_path, "a") as err_log:
                print(err_letters, file=err_log)
            return []
        return result

    @staticmethod
    def validate_date(date: list):
        days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        data_error = "Error! Please, check date"
        if type(date) != list:
            return
        try:
            if date[2] not in range(2021):
                print(data_error)
                raise DateError
            elif date[1] not in days_in_month:
                print(data_error)
                raise DateError
            elif date[0] > days_in_month[date[1]] or date[0] <= 0:
                print(data_error)
                raise DateError
        except DateError as err_date:
            with open(err_log_path, "a") as err_log:
                print(err_date, file=err_log)
            return
        except IndexError as err_index:
            with open(err_log_path, "a") as err_log:
                print(err_index, file=err_log)
            return
        return True


data1 = Date("3-12-2020")
print(data1.extract_number)
print(data1.validate_date(data1.extract_number))


# 2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DevivsionZero(Exception):
    def __init__(self):
        self.text = "Error! Division by zero"
        print(self.text)


try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    if b == 0:
        raise DevivsionZero
    print(f"The division result is {a / b}")
except DevivsionZero as err_dev_zero:
    with open(err_log_path, "a") as err_log:
        print(err_dev_zero, file=err_log)

# 3. Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.


class NotNumbers(Exception):

    def __init__(self):
        self.text = "Error. Please enter the numbers"


user_number = ""
result_list = []
while user_number.lower() != 'stop':
    try:
        user_number = input('Enter number (print "stop" to exit):')
        if user_number.isdigit():
            result_list.append(int(user_number))
    except NotNumbers as error:
        print(error.text)
print(result_list)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod


class Storage:
    pass


class OfficeStorage(Storage):
    storage = {}

    def __init__(self, name):
        self.name = name
        self.departments = []

    def take_for_storage(self, equipment, count, department):
        if department not in self.departments:
            self.departments.append(department)
        if type(count) == str:
            return print("The count must be digit")
        if self.storage.get(equipment) is None:
            self.storage[equipment] = count
        else:
            self.storage[equipment] = self.storage[equipment] + count

    def send_to_department(self, equipment, count, department):
        if department not in self.departments:
            self.departments.append(department)
        if type(count) == str:
            return print("The count must be digit")
        if self.storage.get(equipment) is None:
            self.storage[equipment] = count
        else:
            self.storage[equipment] = self.storage[equipment] - count


class OfficeEquipment:

    def __init__(self, name: str, is_new: bool, cost: float):
        self.name = name
        self.is_new = is_new
        self.cost = cost

    def __str__(self):
        print(self.name)


class Computer(OfficeEquipment):

    def __init__(self, is_new, cost, model: str, cpu_number: int, ram_number: int):
        self.name = "Computer"
        self.model = model
        self.cpu_number = cpu_number
        self.ram_number = ram_number
        super().__init__(name=self.name,
                         is_new=is_new,
                         cost=cost)


class Printer(OfficeEquipment):

    def __init__(self, is_new, cost, model: str, print_speed: int, dpi_number: int):
        self.name = "Printer"
        self.model = model
        self.print_speed = print_speed
        self.dpi_number = dpi_number
        super().__init__(name=self.name,
                         is_new=is_new,
                         cost=cost)


class Scanner(OfficeEquipment):

    def __init__(self, is_new, cost, model: str, scan_speed: int, dpi_number: int):
        self.name = "Scanner"
        self.model = model
        self.scan_speed = scan_speed
        self.dpi_number = dpi_number
        super().__init__(name=self.name,
                         is_new=is_new,
                         cost=cost)


comp1 = Computer(True, 1000, "Dell-3000", 4, 5)
print(comp1.name)
print1 = Printer(True, 500, "Tsx-1000", 60, 600)
print(print1.name)
scan1 = Scanner(False, 100, "Scan123", 10, 300)
print(scan1.name)
storage1 = OfficeStorage("Storage1")
storage1.take_for_storage(comp1, "1", "Some Dep")
storage1.take_for_storage(comp1, 2, "IT")
storage1.send_to_department(comp1, 1, "Trade")
print(storage1.storage)
print(storage1.departments)

# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.
from math import sqrt


class ComplexNumberOperations:
    pass


class ComplexNumber(ComplexNumberOperations):
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine

    def __str__(self):
        if self.real == 0:
            return f"{self.imagine}i"
        elif self.real != 0 and self.imagine > 0:
            return f"{self.real}+{self.imagine}i"
        else:
            return f"{self.real}{self.imagine}i"

    def __add__(self, other):
        self.real = self.real + other.real
        self.imagine = self.imagine + other.imagine
        return ComplexNumber(self.real, self.imagine)

    def __mul__(self, other):
        self.real = (self.real * other.real - self.imagine * other.imagine)
        self.imagine = (self.real * other.imagine + other.imagine * self.real)
        return ComplexNumber(self.real, self.imagine)

    def module(self):
        return f"Complex number module: {sqrt((self.real**2 + self.imagine**2))}"


num1 = ComplexNumber(1, -5)
num2 = ComplexNumber(2, 2)
num3 = ComplexNumber(0, 25)
print(num1)
print(num2)
print(num3)
print(num1 + num2)
print(num1 * num3)