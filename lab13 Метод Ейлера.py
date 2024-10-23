import numpy as np
import matplotlib.pyplot as plt
import sys

def f(x, y):
    return x + np.sin(y / np.sqrt(5))

# Вводимо параметри (ліва, права межі відрізку, крок, початкова умова)
a, b, h, y0 = 1.8, 2.8, 0.1, 2.6

# Перевірка вхідних параметрів
if h <= 0:
    print("Крок h повинен бути позитивним.")
    sys.exit()
if a >= b:
    print("Права межа b повинна бути більшою за ліву межу a.")
    sys.exit()

n = int((b - a) / h)  # кількість кроків

x = np.array([a + i*h for i in range(n + 1)])  # задаємо x генератором списків

y = np.empty(n + 1)
y[0] = y0

for i in range(n):
    y[i + 1] = y[i] + f(x[i], y[i]) * h

y_rounded = np.round(y, 4)  # Округляємо результат
print("x =", x, "\ny =", y_rounded)

plt.plot(x, y, "o", label="точки")
plt.plot(x, y, "red", label="x + sin(y / √5)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Ейлера")
plt.legend()
plt.grid()
plt.show()
