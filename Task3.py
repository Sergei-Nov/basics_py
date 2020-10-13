# 1
def division_func(a, b):
    if b == 0:
        print("You cannot divide by zero")
        return
    return a / b
print(division_func(105, 25))

# 2
def personal_data(user_name, user_surname, user_birth_year, user_city, user_email, user_phone):
    """
    :param user_name: имя пользователя
    :param user_surname: фамилия пользователя
    :param user_birth_year: год рождения пользователя
    :param user_city: город пользователя
    :param user_email: электронная почта пользователя
    :param user_phone: телефон пользователя
    :return: возвращает переменную типа str с данными о пользователе
    """
    result = (f'Пользователь {user_name} {user_surname}, {user_birth_year} года рождения, проживает'
          f' в городе {user_city}, e-mail:{user_email} тел.:{user_phone}')
    return result
# main
print(personal_data(user_name = 'Иван', user_surname = 'Иванов',
                    user_birth_year = '2007', user_city = 'Чита',
                    user_email = 'ivanovIvan@email.ry', user_phone = '+71234567890'))

# 3 Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    result = sum([a, b, c])-min([a, b, c])
    return result
# main
print(my_func(1, 5, 9))

# 4 Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.

def power_func1(x, y = int): # expect y type int
    if type(y) == int and x > 0 and y < 0:
        result = x ** y             # exponentiation with operator **
        #for num in range(abs(y)-1): # exponentiation using multiplication and while loop **
        i = 1
        while i < abs(y):
            x = x * x
            i += 1
        result2 = 1/x
        return result, result2
    else:
        print('"x" must be greater than zero, "y" must be less than zero and an integer')
#main
print(power_func1(3.7,-2))

# 5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
def calc_numbers(user_numbers, numbers_sum):
    """

    :param user_numbers: список из строк введенных пользователем, исключая Q и всё что дальше
    :return: возвращаем сумму листа с числами
    """
    i = 0
    while i < len(user_numbers): # переведём строки в числа
        user_numbers[i] = int(user_numbers[i])
        i += 1
    return sum(user_numbers)

# main
numbers_sum = 0 # сумма чисел в листе
user_numbers = '' # список строк введенных пользователем
result = 0 # общий счётчик суммы всех когда-либо введенных чисел
in_progress = True
while in_progress:
    user_numbers = input('Введите числа разделенные пробелом и нажмите Enter, Q - выход ').upper().split()
    if 'Q' in user_numbers:
        Q_index = user_numbers.index('Q')
        print('Выход')
        in_progress = False
        user_numbers = user_numbers[:Q_index]
    print(f'Сумма введенных чисел: {calc_numbers(user_numbers, numbers_sum)}')
    result = result + calc_numbers(user_numbers, numbers_sum)
    print(f'На данный момент сумма всех введенных чисел: {result}')

# 6
def int_func(word):
    upper_letter = word[0].upper()
    word = upper_letter + word[1:]
    return word
# main
user_text_list = input('Введите текст разделенный пробелами: ').split()
result = ''
for text in user_text_list:
    text = int_func(text)
    result = f'{result} {text}'
print(f'Ваш текст с заглавных букв: {result[1:]}') # выводим результат, убрав пробел перед первым словом