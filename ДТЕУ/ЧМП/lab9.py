import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Дані
x = np.array([1.4, 1.6, 2, 2.5, 3.1])
y = np.array([2.39, 3.85, 2.74, 1.58, 3.15])
n = len(x) - 1
h = np.diff(x)
a = y
b = np.zeros(n)
d = np.zeros(n)
c = np.zeros(n + 1)  # Розширюємо на один елемент для останнього індексу
alpha = np.zeros(n)

for i in range(1, n):      # Обчислення коефіцієнтів
    alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

l = np.ones(n + 1)  # розширюємо l на один елемент
mu = np.zeros(n)
z = np.zeros(n + 1)  # розширюємо z на один елемент

for i in range(1, n):     # пряма хода для знаходження l, mu, z
    l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
    mu[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

# Крайова умова: c[n] = 0
l[n] = 1
z[n] = 0
c[n] = 0

for j in range(n - 1, -1, -1):     # зворотний хід для знаходження c, b, d
    c[j] = z[j] - mu[j] * c[j + 1]
    b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
    d[j] = (c[j + 1] - c[j]) / (3 * h[j])

for i in range(n):     # Виведення аналітичного вигляду кубічного сплайну для кожного відрізка
    print(f"Відрізок {i + 1}:")
    print(f"S_{i}(x) = {a[i]} + {b[i].round(4)}(x - {x[i]}) + {c[i].round(4)}(x - {x[i]})^2 + {d[i].round(4)}(x - {x[i]})^3, x належить [{x[i]}, {x[i + 1]}]")

x_values = np.linspace(np.min(x), np.max(x), 100)  # Діапазон для побудови графіка
y_values = []  # пустий список для значень y сплайну

for i in range(n):      # Обчислення значень сплайна для кожного відрізка
    mask = (x_values >= x[i]) & (x_values <= x[i + 1])
    x_interval = x_values[mask]
    y_interval = a[i] + b[i] * (x_interval - x[i]) + c[i] * (x_interval - x[i]) ** 2 + d[i] * (x_interval - x[i]) ** 3
    y_values.extend(y_interval)     # додає значеня y до загального списку

# Побудова графіка
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, label="Кубічний сплайн", color='b')
plt.scatter(x, y, label="Задані точки", color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

cs = CubicSpline(x, y)     # перевірка за допомогою методу CubicSpline

# Виведення коефіцієнтів сплайну для кожного відрізка
for i in range(len(x) - 1):
    coeffs = cs.c[:, i]  # Коефіцієнти для i-го інтервалу
    spline = f'S_{i + 1}(x) = {coeffs[0]:.4f}*(x - {x[i]})^3 + {coeffs[1]:.4f}*(x - {x[i]})^2 + {coeffs[2]:.4f}*(x - {x[i]}) + {coeffs[3]:.4f}'
    print(spline)

# Генерація нових точок для гладкого графіку сплайна
x_new = np.linspace(np.min(x), np.max(x), 100)
y_new = cs(x_new)

# Побудова графіку
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Точки')
plt.plot(x_new, y_new, label='Кубічний сплайн')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кубічний сплайн')
plt.legend()
plt.grid(True)
plt.show()
