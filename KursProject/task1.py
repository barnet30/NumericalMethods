import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


a = 0
b = 3
h = 0.3
eps = 1e-6
MAX_STEPS = 1000


#Заменить функцию факториала
# def taylor(x):
#     y = 0 # Начало суммы
#     sign = 1 # Знак первого члена ряда
#     s = 1 # Первый член ряда
#     k=0
#     fact_temp = 1
#     while abs(s) > eps and k <= MAX_STEPS:
#         # Прибавляем член к ряду
#         y += sign*s
#         # Вычисляем следующий член ряда
#         k += 1
#         sign = - sign
#         fact_temp *= k
#         denom = fact_temp**2
#         s = ((x*x/4)**k)/denom
#
#     return x, y, k

def taylor(x):
    y = 0  # Начало суммы
    sign = 1  # Знак первого члена ряда
    s = 1  # Первый член ряда
    k = 0
    factorial_temp = 1
    while abs(s) > eps and k <= MAX_STEPS:
        # Прибавляем член к ряду
        y += sign * s
        # Вычисляем следующий член ряда
        k += 1
        sign = sign * (-1)
        factorial_temp *= k
        denom = factorial_temp ** 2
        s = ((x * x / 4) ** k) / denom

    return x, y, k
""" Task 1 """
x_array = []
f_array = []
k_array = []

while a<=b:
    res = taylor(a)
    x_array.append(res[0])
    f_array.append(res[1])
    k_array.append(res[2])
    a += 0.3

table = np.array([x_array,f_array,k_array])

pd.options.display.max_columns = 50
df = pd.DataFrame(table)
print(df)

# plt.plot(x_array,f_array)
# plt.show()
#
# plt.plot()

