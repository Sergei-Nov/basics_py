# 1 Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

filepath = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.1.txt"
print("Enter data and press 'Enter' to add in file. "
      "Enter an empty line to exit ")
with open(filepath, mode="w") as task5_1_test:
    while True:
        user_input = input() + '\n'
        task5_1_test.write(user_input)
        if user_input == '\n':
            break

# 2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

filepath = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.2.txt"
with open(filepath, "r") as task5_2:
    text = task5_2.readlines()
    full_text = '' # переменная для хранения всего текста в файле без пробелов и кареток
    for letters in text:
        str_without_spaces = letters.replace(" ", "") # заменяем пробелы в строках на "ничто"
        result_str = str_without_spaces.replace("\n", "") # заменяем каретки в строках на "ничто"
        full_text += result_str
    print(f"Number of strings in the file: {len(task5_2.readlines())}")
    print(f"Number of symbols in the file: {len(full_text)}")

# 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

filepath = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\salary.txt"
with open(filepath, "r") as salary:
    print("Employees receiving less than 20,000:")
    total_salary = 0 # общая з\п
    workers_count = 0
    for worker in salary:
        employee = worker.split()
        total_salary += int(employee[1])
        wage = int(employee[1])
        workers_count += 1
        if wage < 20000:
            print(employee[0].replace('_', " "))
    print(f"Average salary: {total_salary / workers_count}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

filepath = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.4.txt"
answers_path = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.4_answ.txt"
numbers_dict = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}
with open(filepath, "r") as task5_4:
    for lines in task5_4:
        new_line = lines.replace('\n', '')
        num_word = numbers_dict[new_line[-1:]]
        with open(answers_path, 'a') as answers:
            print(f"{num_word} - {new_line[-1]}", file=answers)
print("Answers written to file Task5.4_answ.txt")

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

filepath = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.5.txt"

with open(filepath, "w") as task5_6:
    numbers_str = input("Enter numbers: ")
    task5_6.write(numbers_str)
with open(filepath, "r") as readnumbers:
    sum_numbers = 0
    for num in readnumbers:
        number_list = num.split()
        try:
            for number in number_list:
                number = int(number)
                sum_numbers += number
        except ValueError:
            print("Error! There are letters in the file!")
    print(f"Sum of numbers in file: {sum_numbers}")

# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# P.S Более лаконичного решения к сожалению не придумал, возможно наговнокодил, поэтому добавляю кучу комментов :(
file_path = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.6.txt"
with open(file_path, "r", encoding="UTF-8") as task5_6:
        data_list = task5_6.readlines()
        result_dict = {} # сюда запишем ответ на задачу
        for el in data_list: # цикл делит каждую строку текстового файла на списоки вида: [название_дисцеплины, 100, 50(пр), 20(лаб).]
            el_splited = el.split()
            dis_name = el_splited[0]
            letters = '' # строка в которой хранится строка из всех интовых элементов списка data_list разделенных пробелами
            for letter in el: # цикл проходится по каждой букве\цифре в списке el
                # ниже программа отлавливает пробелы и добавляет их в итоговую строку letters, все другие символы
                # пытаемся перевести в int, если неудачно отлавливаем ошибку ValueError и пропускаем эту букву
                # если удачно перевели в int, добавляем в строку letters
                try:
                    if letter == " ":
                        letters += letter
                    else:
                        letter = int(letter)
                        letters += str(letter)
                except ValueError:
                    pass
            result_numbers_list = letters.split() # лист чисел (без лишних знаков)
            result_sum = 0 # сумма часов по дисциплине
            for number in result_numbers_list:
                number = int(number)
                result_sum += number
            result_dict[dis_name] = result_sum # добавляем элемент в словарь
        print(result_dict)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

filepath = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.7.txt"
with open(filepath, "r") as task_7:
    result_dict = {}
    result_json = []
    profit_dict = {}
    firms_list = task_7.readlines() # лист из фирм
    sum_profit = 0 # общая прибыль всех фирм
    for firm in firms_list:
        company_list = firm.split()
        firm_name = company_list[0]
        firm_profit = int(company_list[2]) - int(company_list[3])
        sum_profit += firm_profit
        result_dict[firm_name] = firm_profit # добавляем ключ с именем фирмы и значением прибыли
    average_profit = sum_profit / len(result_dict)
    profit_dict["average_profit"] = int(average_profit)
    result_json.append(result_dict)
    result_json.append(profit_dict)
    result_json_path = r"C:\Users\sergei.novikov\Documents\GitRep\basics_py\Task5\Task5.7_result.json"
    with open(result_json_path, "w") as result:
        print(result_json, file=result)

