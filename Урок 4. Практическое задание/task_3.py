"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    temp_list = list(str(enter_num))
    temp_list.reverse()
    return ''.join(temp_list)

def main():
    revers_1(12345)
    revers_2(12345)
    revers_3(12345)
    revers_4(12345)

print(timeit("revers_1(12345)", globals=globals()))
print(timeit("revers_2(12345)", globals=globals()))
print(timeit("revers_3(12345)", globals=globals()))
print(timeit("revers_4(12345)", globals=globals()))

run('main()')

"""
Через cProfile просмотр не показателен, потому что операция слишком быстрая в любом варианте из четырех.
Самая долгая реализация - через рекурсию, т.к. рекурсия сначала набивает стэк. Далее цикл. Примененные в 
4 варианте встроенные функции работают быстрее, но еще быстрее срез, т.к. меньше операций.
"""
