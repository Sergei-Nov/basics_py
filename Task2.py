# 1 Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента

my_list = [1, 'some text', None, True, 3.14, [1, 2, 3], { 1: 'one'}, (3, 2, 1), {"a", "b"}]
for type_of_date in my_list:
    print(type(type_of_date))

#2 Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

count_of_numbers = int(input('Введите число элементов списка: '))
print('Вводите числа для списка')
i = 0
my_list = []
while i < count_of_numbers:
    my_list.append(input('Введите число: '))
    i += 1
print(my_list)
i = 0
while i < count_of_numbers - 1: ## -1 так как последний нечетные элемент нужно оставить на месте
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2
print(my_list)


# 3.1 (через list) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
months = [['январь', 'зиме'], ['ферваль', 'зиме'], ['март', 'весне'], ['апрель', 'весне'],
['май', 'весне'], ['июнь', 'весне'], ['июль', 'лету'], ['август', 'лету'],
['сентябрь', 'осени'], ['октябрь', 'осени'], ['ноябрь', 'осени'], ['декабрь', 'зиме']]
# ниже отнимаю 1, чтобы число от пользователя было от 0 до 11 и соответствовало индексам списка
month_number = int(input('Введите номер месяца: ')) - 1
print(f'Месяц {months[month_number][0]} относится к {months[month_number][1]}')

# 3.2 (через dict)
months = {1: ['январь', 'зиме'], 2: ['ферваль', 'зиме'], 3: ['март', 'весне'], 4: ['апрель', 'весне'],
          5: ['май', 'весне'], 6: ['июнь', 'весне'], 7: ['июль', 'лету'], 8: ['август', 'лету'],
          9: ['сентябрь', 'осени'], 10: ['октябрь', 'осени'], 11: ['ноябрь', 'осени'], 12: ['декабрь', 'зиме']}
month_number = int(input('Введите номер месяца: '))
print(f'Месяц {months[month_number][0]} относится к {months[month_number][1]}')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
words = input('Enter your text: ').split()
for word in words:
    print(word[:10])

# 5.  Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
rating_list = [7, 5, 3, 3, 2]
i = 0
number = int(input('Enter number to add in rating: '))
for num in rating_list:
    if number <= num:
        i += 1
rating_list.insert(i, number)
print(rating_list)

# 6.
from copy import deepcopy
goods = [] # структура для хранения товаров
dict = {"название": "", "цена": 0, "количество": 0, "ед": ""} # макет словаря
analytics = {"название": [], "цена": [], "количество": [], "ед": []}
count_of_goods = 0 # число товаров
in_progress = True # переменная статуса программы (True - юзер все еще вносит товары, False - уже внёс)
while in_progress:
    if input("Для продолжения введите любой символ кроме 'Q': ").upper() == "Q":
        break
    count_of_goods += 1
    # заполняем словарь
    for charact in dict:
        user_input = input(f"Введите значение для поля {charact}: ")
        dict[charact] = int(user_input) if charact in {"цена", "количество"} else user_input
        analytics[charact].append(dict[charact])
    goods.append((count_of_goods, deepcopy(dict)))  # добавляем кортеж, состоящий из числа и словаря в структуру goods
    print(f"В базу данных добавлено {count_of_goods} товаров.")
    for good in goods:
        print(good)
    print(f'Аналитика: \n{"-" * 20}')
    for key, value in analytics.items():
        print(f'{key:>10}: {value}')
    print("-" * 20)