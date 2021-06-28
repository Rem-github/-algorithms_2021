"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

def func_3(nums):
    new_arr = [n[0] for n in enumerate(nums) if n[1] % 2 == 0]
    return new_arr


print(timeit("func_1([1,2,3,4,5,6,7,8,9])", globals=globals()))
print(func_1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(timeit("func_2([1,2,3,4,5,6,7,8,9])", globals=globals()))
print(func_2([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(timeit("func_3([1,2,3,4,5,6,7,8,9])", globals=globals()))
print(func_3([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# почему-то у меня не получилось ускорить процесс с помощью lc и enumerate
