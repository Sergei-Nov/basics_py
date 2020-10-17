from sys import argv

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
script_name, first_param, second_param, third_param = argv

def salary(hours, rate, prize):
    return int(hours) * int(rate) + int(prize)

print(f'Your parameters: {argv[1]} hours, {argv[2]} rub/hour and {argv[3]} rub prize.\n'
      f'Calculated salary: {salary(argv[1], argv[2], argv[3])} rubles')