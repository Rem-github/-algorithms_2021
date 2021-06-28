"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from collections import Counter
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    el = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {el[0]}, ' \
           f'оно появилось в массиве {el[1]} раз(а)'


def func_4():
    for number, count in Counter(array).items():
        if count > 1:
            return f'Число {number} повторяется {count} раза'


print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("func_3()", globals=globals()))
print(timeit("func_4()", globals=globals()))
print(timeit("func_4()", globals=globals()))

# Сделал 2 варианта через Counter, но это оказалось не самым быстрым решением, хотя код короче