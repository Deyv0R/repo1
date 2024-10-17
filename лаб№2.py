import numpy as np
from scipy.misc import derivative

def f(x):
    return 3 * pow(x, 4) + 2 * pow(x, 3) + pow(x, 2) + x - 5

eps = 0.0001 # задання точності для числових методів

def find_segments():
    search_range = np.arange(-10, 10, 1) # генерація діапазону значень
    segments = []
    previous_x = None

    for x in search_range:
        x = round(x, 4)
        current_x = f(x)

        if previous_x is not None and previous_x * current_x < 0:    # перевірка зміни знаку функції
            segments.append((a, x))    # збереження відрізку, де функція змінює знак

        a = x
        previous_x = current_x

    return segments

segments = find_segments()
for a, b in segments:
    print(f'Найдений сегмент: [{a}, {b}]')

def rec(a, b, eps):      #реалізація методу половинного ділення для знаходження кореня
    while abs(a - b) > eps:
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    print('x =', round(x, 5), ' - Метод половинного ділення')

def hord(a, b, eps):      #реалізація методу хорд для знаходження кореня
    if f(a) * derivative(f, a, n=2) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a

    xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))   # обчислення нової точки методом хорд
    
    while abs(xi_1 - xi) > eps:   # цикл до досягнення необхідної точності
        xi = xi_1
        xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))

    print('x =', round(xi_1, 5), ' - Метод Хорд')     # виведення результату

a = 0.
b = 1.
print(f"Розв'язання нелінійного рівняння на відрізку [{a}, {b}]")  # виведення інформації
rec(a, b, eps)
hord(a, b, eps)
