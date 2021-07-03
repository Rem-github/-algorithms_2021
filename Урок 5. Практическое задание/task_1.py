"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple

def year_profit(user_list):
    return user_list.profit_1 + user_list.profit_2 + user_list.profit_3 + user_list.profit_4


company_profit = namedtuple('company_profit', 'name, profit_1 profit_2 profit_3 profit_4')
company_list = []
profit_year_all = 0
n = int(input('Введите количество предприятий: '))
for i in range(n):
    company_list.append(company_profit(
                      name=input('Введите название компании: '),
                      profit_1=int(input('Введите прибыль первого квартала: ')),
                      profit_2=int(input('Введите прибыль второго квартала: ')),
                      profit_3=int(input('Введите прибыль третьего квартала: ')),
                      profit_4=int(input('Введите прибыль четвертого квартала: '))
    ))
    profit_year_all += year_profit(company_list[i])
avg_profit_year_all = profit_year_all/n
for i in range(n):
    if year_profit(company_list[i]) > avg_profit_year_all:
        print(f'Прибыль компании {company_list[i].name} выше среднего значения')
    elif year_profit(company_list[i]) < avg_profit_year_all:
        print(f'Прибыль компании {company_list[i].name} ниже среднего значения')

