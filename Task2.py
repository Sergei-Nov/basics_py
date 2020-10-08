# # 1 Создать список и заполнить его элементами различных типов данных.
# # Реализовать скрипт проверки типа данных каждого элемента
# my_list = [1, 'some text', None, True, 3.14, [1, 2, 3], { 1: 'one'}, (3, 2, 1), {"a", "b"}]
# for type_of_date in my_list:
#     print(type(type_of_date))

#2 Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# 3.1 (через list) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# months = ['январь', 'ферваль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# # ниже отнимаю 1, чтобы число от пользователя было от 0 до 11 и соответствовало индексам списка
# month_number = int(input('Введите номер месяца: ')) - 1
# if month_number == 11 or month_number >= 0 and month_number < 2:
#     print(f'{months[month_number]} относится к зиме')
# elif month_number >= 2 and month_number < 5:
#     print(f'{months[month_number]} относится к весне')
# elif month_number >= 5 and month_number < 8:
#     print(f'{months[month_number]} относится к лету')
# elif month_number >= 8 and month_number < 11:
#     print(f'{months[month_number]} относится к осени')

# # 3.2 (через dict) более лакончино решить не удалось
# months = {1: 'январь', 2: 'ферваль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
#           7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
# # month_number = int(input('Введите номер месяца: '))
# if month_number == 12 or month_number >= 1 and month_number < 3:
#     print(f'{months[month_number]} относится к зиме')
# elif month_number >= 3 and month_number < 6:
#     print(f'{months[month_number]} относится к весне')
# elif month_number >= 6 and month_number < 9:
#     print(f'{months[month_number]} относится к лету')
# elif month_number >= 9 and month_number < 12:
#     print(f'{months[month_number]} относится к осени')

