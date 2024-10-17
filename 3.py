# Побудова графіка функції
import numpy as np
import matplotlib.pyplot as plt

# Область значень для x та y
x_min, x_max = -1, 1
y_min, y_max = -4, 1
step = 0.01

# Створюємо масиви значень x та y
x, y = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

# Рівняння системи
eq1 = 3 * x - np.cos(y) - 0.9
eq2 = np.sin(x - 0.6) - y - 1.6

# Створюємо графік
fig, ax = plt.subplots(figsize=(10, 10))

# Додаємо графік першого рівняння
ax.contour(x, y, eq1, levels=[0], colors='red')

# Додаємо графік другого рівняння
ax.contour(x, y, eq2, levels=[0], colors='blue')

# Налаштування графіка
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графік системи рівнянь')
plt.grid(True)

# показує графік
plt.show()

import numpy as np
from scipy import optimize

x0 = 0.15
y0 = -2.1
delta = 0.1

def f1(y):
    return (1/3) * np.cos(y) + 0.3  

def f2(x):
    return np.sin(x - 0.6) - 1.6  

def iter_method(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while (abs(xn1 - xn) >= e) and (abs(yn1 - yn) >= e):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print('Проста ітерація:')
    print('x =', xn, '\ny =', yn, '\nКількість ітерацій =', n)

iter_method(x0, y0, 0.0001)

def f3(x):  # Задаємо функцію для перевірки
    return [3*x[0] - np.cos(x[1]) - 0.9, np.sin(x[0] - 0.6) - x[1] - 1.6]

s = optimize.root(f3, [0., 0.], method='hybr')
print('Перевірка', s.x)
