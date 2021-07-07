"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random

# второй вариант реализации "по восходящей", без рекурсии
# с ростом списка время варианта "по восходящей" увеличивается по отношению к варианту "по нисходящей"
# но рекурсия задействует больше памяти

def merge(s1, s2):
    r = []
    i, j = 0, 0
    while (True):
        if i >= len(s1):
            r += s2[j:]
            break
        if j >= len(s2):
            r += s1[i:]
            break
        if s1[i] < s2[j]:
            r += [s1[i]]
            i += 1
        else:
            r += [s2[j]]
            j += 1
    return r


# собственно сортировка

def merge_sort(x):
    xx = []  # превращаем каждый элемент в список
    for a in x:
        xx = xx + [[a]]
    while (True):
        k = len(xx)  # когда остался единственный список - конец
        if k == 1:
            break
        yy = []
        i = 0
        j = 1
        while (True):  # строим списки пар, потом четверок и т.п.
            if i == k:
                break
            if j == k:
                yy += [xx[i]]
                break
            else:
                yy += [merge(xx[i], xx[j])]
            i += 2
            j += 2

        xx = yy
    return xx[0]


orig_list = [random.random()*100 for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list))
# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [random.random()*100 for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [random.random()*100 for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list)",
        globals=globals(),
        number=1000))


# базовый код

def merge_sort_base(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_base(left)
        merge_sort_base(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


orig_list = [random.random()*100 for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list))
# замеры 10
print(
    timeit.timeit(
        "merge_sort_base(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.random()*100 for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort_base(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.random()*100 for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort_base(orig_list[:])",
        globals=globals(),
        number=1000))
