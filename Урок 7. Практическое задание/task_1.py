"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random


def bubble_sort(lst_obj):  # доработанная функция
    n = 1
    res_list = []
    while len(lst_obj) != 0:
        for i in range(len(lst_obj)-1):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        ch = lst_obj.pop()
        res_list.append(ch)
        n += 1
    return res_list
# доработка в уменьшении числа переборов списка, за счет отбрасывания уже отсортированных элементов
# на коротких списках получили увеличение скорости, на длинных скорость ухудшилась за счет времени работы с вторым списком

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
# замеры 10
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))


def bubble_sort1(lst_obj):  # базовая функция
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort1(orig_list))
# замеры 10
print(
    timeit.timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))

"""
[22, -1, -43, 98, -51, 73, -76, -86, 9, 99]
[99, 98, 73, 22, 9, -1, -43, -51, -76, -86]
0.00014279999999999848
0.6272441000000001
53.499709300000006
[53, 88, -18, 8, 13, -93, 72, -54, 65, -53]
[-93, -54, -53, -18, 8, 13, 53, 65, 72, 88]
0.0041703999999995744
0.4676220999999998
52.8172704
"""
