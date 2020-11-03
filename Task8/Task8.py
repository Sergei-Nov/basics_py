# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

class Storage:

    @abstractclass



class OfficeEquipment:

    def __init__(self, name: str, is_new: bool, cost: float):
        self.name = name
        self.is_new = is_new
        self.cost = cost


class Computer(OfficeEquipment):

    def __init__(self, name, is_new, cost, model: str, cpu_number: int, ram_number: int):
        self.name = "Computer"
        self.model = model
        self.cpu_number = cpu_number
        self.ram_number = ram_number
        super().__init__(name=name,
                         is_new=is_new,
                         cost=cost)


class Printer(OfficeEquipment):

    def __init__(self, name, is_new, cost, model: str, print_speed: int, dpi_number: int):
        self.model = model
        self.print_speed = print_speed
        self.dpi_number = dpi_number
        super().__init__(name=name,
                         is_new=is_new,
                         cost=cost)


comp1 = Computer("PC1", True, 1000, "Dell-3000", 4, 5)
print(comp1.name)
print1 = Printer("Printer1", True, 500, "Tsx-1000", 60, 600)
print(print1.model)
c = 1