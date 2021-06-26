"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def time_calc(user_func):
    def calc(*args, **kwargs):
        start_time = time.time()
        user_func(*args, **kwargs)
        end_time = time.time() - start_time
        return end_time
    return calc


@time_calc
def list_add(n):
    for i in range(n):
        user_list.append(i/5)           # O(1)


@time_calc
def dict_add(n):
    for i in range(n):
        user_dict[i] = i/5              # O(1)


@time_calc
def dict_list_ins(n):
    user_list1 = []
    for i in range(n):
        user_list1.insert(0, i/5)       # O(n)


@time_calc
def list_search(user_list):             # O(n^2)
    f = 0
    for i in range(len(user_list)):     # O(n)
        if i in user_list:              # O(n)
            f = 1


@time_calc
def dict_search(user_dict):             # O(n^2)
    f = 0
    for k in user_dict:                 # O(n)
        if k in user_dict:              # O(n)
            f += 1


user_list = []
user_dict = {}
print(list_add(20000))
print(dict_add(20000))
print(dict_list_ins(20000))

# при аналогичных по сложности вариантах заполнения, словарь заполняется немного дольше, вероятно потому
# что в ячейки памяти заносятся два элемента - ключ и значение.
# при заполнении списка через insert, функция выполняется значительно дольше

print(list_search(user_list))
print(dict_search(user_dict))

# для словаря поиск выполняется значительно быстрее чем для списка