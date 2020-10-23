# 1 Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
# метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод

from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color = "red"

    def running(self):
        self.__color = {"red": 7, "yellow": 2, "green": 5}
        for el in cycle(self.__color):
            print(f"***{el.upper()}***")
            sleep(self.__color[el])


Light1 = TrafficLight()
Light1.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:

    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width

    def asf_mass(self, mass_for_meter, centimeters):
        return self.length * self.width * mass_for_meter * centimeters

mass_for_meter = int(input("Enter the amount of asphalt per square meter of canvas: "))
centimeters = int(input("Enter the amount of asphalt per centimeter of road thickness: "))
some_road = Road(mass_for_meter, centimeters)
print(f"This road will require asphalt: {some_road.asf_mass(10, 15)} tons")

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        self.full_name = f"{self.name} {self.surname}"
        return self.full_name

    def get_total_income(self):
        self.total_income = int(self._income["wage"])+int(self._income["bonus"])
        return self.total_income

lobby_boy = Position('Ivan','Ivanov','foodboy',100,50)
print(lobby_boy.get_full_name())
print(lobby_boy.get_total_income())

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
        self.car_rides = False

    def go(self, speed):
        if self.car_rides:
            print(f"{self.name} is already driving")
            return
        self.car_rides = True
        self.speed = speed
        print(f"{self.name} rides")
        self.show_speed()

    def stop(self):
        if not self.car_rides:
            print(f"{self.name} has already stopped")
            return
        self.car_rides = False
        self.speed = 0
        print(f"{self.name} stopped")
        self.show_speed()

    def turn(self, direction):
        print(f"{self.name} turned to the {direction}")

    def show_speed(self):
        print(f"{self.name} speed -{self.speed}-")


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print("Over speed!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print("Over speed!")


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(name=name, color=color)
        self.color = color
        self.is_police = True


car1 = SportCar("red", "Tesla-X")
car1.go(50)
car1.turn("left")
car1.turn("right")
car1.go(50)
car1.stop()
car1.stop()
police_car = PoliceCar("Blue", "PoliceCar1")
police_car.go(500)
police_car.turn("left")
police_car.turn("right")
police_car.stop()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start draw")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}: Pen drawing started")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}: Pencil drawing started")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}: Handle drawing started")


pen1 = Pen("Pen #1")
pen1.draw()
pencil1 = Pencil("Pencil #1")
pencil1.draw()
handle1 = Handle("Handle #1")
handle1.draw()
