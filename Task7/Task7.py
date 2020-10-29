# 1 Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from abc import ABC, abstractmethod


class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix = ""
        for matrix_string in self.data:
            for element in matrix_string:
                matrix += f"{element} "
            matrix += "\n"
        return f"Matrix is:\n{matrix}"

    def __add__(self, other):
        num_strings = len(self.data) # кол-во строк в матрице
        num_column = len(self.data[0]) # кол-во столбцов в матрице
        str_counter = 0 # счётчик строк
        while str_counter < num_strings:
            column_counter = 0
            while column_counter < num_column:
                self.data[str_counter][column_counter] = self.data[str_counter][column_counter] + other.data[str_counter][column_counter]
                column_counter += 1
            str_counter += 1
        return Matrix(self.data)


some_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat1 = Matrix(some_matrix)
print(mat1)
mat2 = Matrix(some_matrix)
mat3 = mat1+mat2

#2 Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes(ABC):
    @abstractmethod
    def calc_textile(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calc_textile(self):
        return round(self.size / 6.5 + 0.5, 2)

    @staticmethod
    def calc_all_textile(data):
        all_textile = 0
        for i in data:
            all_textile += i.calc_textile
        return f"To sew {len(data)} units of clothing, you need {all_textile} units of textiles"


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calc_textile(self):
        return round(2 * self.height + 0.3, 2)

    @staticmethod
    def calc_all_textile(data):
        all_textile = 0
        for i in data:
            all_textile += i.calc_textile
        return f"To sew {len(data)} units of clothing, you need {all_textile} units of textiles"


coat1 = Coat(36)
print(coat1.calc_textile)
costume1 = Costume(1.9)
print(costume1.calc_all_textile([coat1, costume1]))

# 3 Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.
# 1. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# 2.Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# 3. Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# 4. Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        if type(other.count) == int:
            return Cell(self.count + other.count)
        else:
            raise ValueError("Error, number must be integer")

    def __sub__(self, other):
        if type(other.count) == int:
            if self.count - other.count > 0:
                return Cell(self.count - other.count)
            else:
                print("Cant substract")
        else:
            raise ValueError("Error, number must be integer")

    def __mul__(self, other):
        if type(other.count) == int:
            return Cell(self.count * other.count)
        else:
            raise ValueError("Error, number must be integer")

    def __truediv__(self, other):
        return Cell(round(self.count - other.count))

    def __str__(self):
        return self.make_order

    @property
    def make_order(self):
        cells_in_line = 5
        lines_count = self.count // cells_in_line
        cells_in_last_line = self.count % cells_in_line
        lines = f'{"*" * cells_in_line}\n' # строки с кол-вом ячеек кратным cell_in_line
        last_line = f'{"*" * cells_in_last_line}' # последняя строка
        return f'{lines_count * lines}{last_line}'


cell1 = Cell(3)
cell2 = Cell(2)
new_cell = cell1 + cell2
new_cell2 = cell1 - cell2
new_cell3 = cell1 * cell2
new_cell4 = cell1 / cell2
print(new_cell)
print(new_cell2)
print(new_cell3)
print(new_cell4)

