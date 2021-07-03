"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint


def dict_create(n):
    user_dict = {}
    for i in range(n):
        user_dict[i] = i/2
    return user_dict


def ord_dict_create(n):
    user_ord_dict = OrderedDict()
    for i in range(n):
        user_ord_dict[i] = i/2
    return user_ord_dict


def dict_change(user_dict):
    for i in range(20):
        user_dict[randint(0, 30)] = i/3
    return user_dict


def ord_dict_change(user_ord_dict):
    for i in range(20):
        user_ord_dict[randint(0, 30)] = i/3
    return user_ord_dict


print(timeit("dict_create(50)", globals=globals()))     # обычный словарь заполняется значительно быстрее
print(timeit("ord_dict_create(50)", globals=globals()))
user_dict = dict_create(50)
user_ord_dict = ord_dict_create(50)
print(timeit("dict_change(user_dict)", globals=globals()))     # замена случайных элементов одинакова по скорости
print(timeit("ord_dict_change(user_ord_dict)", globals=globals()))

# Вывод: использование OrderedDict имеет смысл только там, где необходимы его специальные функции