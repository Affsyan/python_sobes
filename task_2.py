"""
Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os
from os.path import isfile


def print_directory_contents(s_path):
    list_dir = [s_path]
    for path_dir in list_dir:
        for name in os.listdir(path_dir):
            if isfile(os.path.join(path_dir, name)):
                print(f'{path_dir} {name}')
            else:
                list_dir.append(os.path.join(path_dir, name))


print_directory_contents(input('Введите путь каталога: '))



