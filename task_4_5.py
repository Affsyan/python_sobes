"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""
import os


def create_file(file_name):
    file_name += '.txt'
    if file_name in os.listdir(os.getcwd()):
        print("Файл уже существует.")
    else:
        number_list = [str(i) for i in range(1, 15)]
        text_list = ['test' for _ in range(1, 15)]
        print(number_list)
        print(text_list)
        path = os.getcwd() + '\\' + file_name
        with open(path, 'w', encoding='UTF-8') as f:
            f.write('\n'.join(y + x for x, y in zip(number_list, text_list)))
        reed_file(path)


def reed_file(file_path):
    wanted_symbol = 'test13'
    counter = 0
    wanted_symbol_list = []
    with open(file_path, 'r', encoding='UTF-8') as q:
        for line in q:
            line = line.strip()
            counter += 1
            if line == wanted_symbol:
                wanted_symbol_list.append([wanted_symbol_list, counter])
        counter = 0
        for _ in wanted_symbol_list:
            if counter == 0:
                print(f'Первое вхождение элемента {wanted_symbol} на строке {_[1]}')
                counter += 0
            else:
                print(f'Элемент {wanted_symbol} найден на строке {_[1]}')

    with open(file_path, 'r', encoding='UTF-8') as e:
        old_data = e.read()

    with open(file_path, 'w', encoding='UTF-8') as f:
        new_data = old_data.replace(wanted_symbol, '123test')
        f.write(new_data)


create_file(input('Введите имя файла: '))
