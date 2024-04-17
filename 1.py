"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os

fullpath = "D:\GeekBrains data science в медицине\материалы\погружение в python\семинары\dz5\task2.py"

def info_path(path_str: str) -> tuple:
    path, filename = os.path.split(path_str)
    filename, extension = filename.split('.')
    return path, filename, extension

print({info_path(fullpath)})