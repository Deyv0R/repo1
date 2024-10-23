import numpy as np
import matplotlib.pyplot as plt

# Функція для правої частини диференціального рівняння
def f(x, y):
    return x + np.cos(y / 3)

a = 1.6  
b = 2.6  
h = 0.1  
y0 = 4.6  
n = int((b - a) / h)  # кількість кроків

# Генерація x без останнього значення
x = np.arange(a, b + h, h)  

y = np.empty(n + 1)  # Масив для значень y, з індексами до n включно
y[0] = y0

# Метод Ейлера-Коші
for i in range(n):
    y[i + 1] = y[i] + (f(x[i], y[i]) + f(x[i + 1], y[i] + h * f(x[i], y[i]))) * h / 2

# Округлення результату
y_rounded = np.round(y, 4)

print("x =", x)
print("y =", y_rounded)

# Побудова графіка
plt.plot(x, y, "o", label="Точки") 
plt.plot(x, y, "r-", label="x + cos(y / 3)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Ейлера-Коші для y' = x + cos(y / 3)")
plt.legend()
plt.grid()
plt.show()
