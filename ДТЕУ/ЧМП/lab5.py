import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x_min, x_max = -3, 2
y_min, y_max = -4, 2
step = 0.001

x, y = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))       # створює масиви

eq1 = np.sin(y + 1) - x - 1.2
eq2 = 2 * y + np.cos(x) - 2

fig, ax = plt.subplots(figsize=(10, 10))     # створює графік

ax.contour(x, y, eq1, levels=[0], colors='red')   # контурний графік першого рівняння

ax.contour(x, y, eq2, levels=[0], colors='blue')    # контурний графік другого рівняння

# налаштування графіка
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графік системи рівнянь')
plt.grid(True)

plt.show()

# метод простої ітерації

x0 = 0.15
y0 = -2.1

def f1(x): # функція для обчислення значення y на основі x
    return (2 - np.cos(x)) / 2  

def f2(y): # функція для обчислення значення x на основі y
    return np.sin(y + 1) - 1.2  

def iter_method(x, y, e): # функція для реалізації методу простої ітерації
    xn = x
    yn = y
    xn1 = f2(yn)  
    yn1 = f1(xn)  
    n = 1
    while (abs(xn1 - xn) >= e) and (abs(yn1 - yn) >= e): # цикл повторюється, поки x і y не стануть меншими за задану точність
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print('Проста ітерація:')
    print('x =', xn, '\ny =', yn, '\nКількість ітерацій =', n)

iter_method(x0, y0, 0.0001)

def f3(x):  # функція для перевірки рішення
    return [np.sin(x[1] + 1) - x[0] - 1.2, 2 * x[1] + np.cos(x[0]) - 2]

s = optimize.root(f3, [0., 0.], method='hybr')
print('Перевірка', s.x)
