"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import time
import memory_profiler

# декоратор для измерения времени и памяти
def time_mem_calc(user_func):
    def calc(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = time.time()
        user_func(*args, **kwargs)
        end_time = time.time() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Время выполнения задачи: {end_time} c, дополнительная память {mem_diff} MiB'
    return calc

# первый вариант

@time_mem_calc
def func(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# @time_mem_calc
def func_g(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i


@time_mem_calc
def pnt_g(nums):
    for el in func_g(nums):
        print(el)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(func(num))
# Время выполнения задачи: 0.0 c, дополнительная память 0.01171875 MiB
print(func_g(num))
print(pnt_g(num))
# Время выполнения задачи: 0.0 c, дополнительная память 0.0 MiB
# Генератор использует ресурсы в момент вызова будет выдавать по 1 элементу,
# что значительно экономит память


# второй вариант


def list_create_end(n):
    user_list = []
    for i in range(n):
        user_list.append(i)
    return user_list


@time_mem_calc
def list_change(user_list):
    for i in range(n):
        user_list[i] = str(i)
    return user_list


@time_mem_calc
def list_change_map(user_list):
    user_list = list(map(str, user_list))
    return user_list


n = 5000000
user_list = list_create_end(n)
print(list_change(user_list))
# Время выполнения задачи: 0.8317756652832031 c, дополнительная память 155.046875 MiB
print(list_change_map(user_list))
# Время выполнения задачи: 0.5375561714172363 c, дополнительная память 0.02734375 MiB
# В случае использования функции map время выполнения ниже и затраты памяти значительно меньше

# третий вариант


class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        st = ''
        for el in self.matrix_list:
            for num in el:
                st += str(num) + ' '
            st +='\n'
        return f'{st}'

    def __add__(self, other):
        new_list = []
        if len(self.matrix_list) == len(other.matrix_list):
            for el in range(len(self.matrix_list)):
                if len(self.matrix_list[el]) == len(other.matrix_list[el]):
                    new_list.append([])
                    for j in range(len(self.matrix_list[el])):
                        new_list[el].append(self.matrix_list[el][j] + other.matrix_list[el][j])
                else:
                    return f'Матрицы разного размера'
        else:
            return f'Матрицы разного размера'
        return Matrix(new_list)


@time_mem_calc
def sum_matrix():
    x = Matrix([[1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],[1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],
                [1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],[1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],
                [1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],[1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],
                [1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3],[1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3]])
    y = Matrix([[0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],[0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],
                [0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],[0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],
                [0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],[0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],
                [0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0],[0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0]])
    #print(x)
    #print(y)
    z = x + y
    print(z)


print(sum_matrix())

# я хотел испытать __slots__ но подходящего задания с ООП я не нашел в тех заданиях которые мы делали
# время выполнения и дополнительная память 0