"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

user_db = {
    'Ромашка': 100000,
    'Роскосмос': 1000000000,
    'Магнолия': 50000,
    'ПочтаРоссии': 100,
    'ВыпускникиГикбрэйнс': 2
}

# в данном варианте сложность такого алгоритма: O(n) - линейная.
def max1(user_db):
    k = ''                                       # O(1)
    tmp = {}                                     # O(1)
    for i in range(3):                           # O(1)
        for key, value in user_db.items():       # O(n)
            if value == max(user_db.values()):   # O(n)
                k = key                          # O(1)
                tmp.update({key : value})        # O(1)
        user_db.pop(k)                           # O(1)
    return tmp                                   # O(1)

# в данном варианте сложность такого алгоритма: O(n^2) - квадратичная.
def max2(user_db):
    i = 0                                        # O(1)
    while( (len(user_db) - i) >= 3):             # O(n)
        for key, value in user_db.items():       # O(n^2)
            if value == min(user_db.values()):   # O(n)
                k = key                          # O(1)
        user_db.pop(k)                           # O(1)
        i += 1                                   # O(1)
    return user_db                               # O(1)

# Первое решение более простое и быстрое, потому что линейная зависимость значительно лучше квадратичной

print(max2(user_db))