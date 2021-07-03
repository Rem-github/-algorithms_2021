"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from timeit import timeit
from collections import deque
from random import randint


def list_create_1(n):
    user_list = []
    for i in range(n):
        user_list.insert(0, i)
    return user_list


def deq_create_1(n):
    user_deq = deque()
    for i in range(n):
        user_deq.appendleft(i)
    return user_deq


def list_create_end(n):
    user_list = []
    for i in range(n):
        user_list.append(i)
    return user_list


def deq_create_end(n):
    user_deq = deque()
    for i in range(n):
        user_deq.append(i)
    return user_deq


def list_pop():
    user_list = list_create_end(50)
    return user_list.pop()


def deq_pop():
    user_deq = deq_create_end(50)
    return user_deq.pop()


def list_change():
    user_list = list_create_end(50)
    for i in range(50):
        user_list[randint(0, 30)] = i


def deq_change():
    user_deq = deq_create_end(50)
    for i in range(50):
        user_deq[randint(0, 30)] = i


print(timeit("list_create_1(50)", globals=globals()))  # insert работает гораздо дольше
print(timeit("deq_create_1(50)", globals=globals()))
print(timeit("list_create_end(50)", globals=globals()))  # при вставке в конец время почти одинаковое
print(timeit("deq_create_end(50)", globals=globals()))
print(timeit("list_pop()", globals=globals()))  # при удалении последнего элемента время почти одинаковое
print(timeit("deq_pop()", globals=globals()))
print(timeit("list_change()", globals=globals()))  # при замене случайных элементов время почти одинаковое
print(timeit("deq_change()", globals=globals()))
