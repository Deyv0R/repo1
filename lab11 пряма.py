import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**2 * np.sin(x)

# Вхідні дані
x = np.array([i * 0.1 for i in range(0, 9)])  # Можна збільшити кількість точок
y = np.array([func(xi) for xi in x])

print('x=', x)
print('y=', y)

# Обчислення коефіцієнтів a та b для лінії y = ax + b
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
b = y_mean - a * x_mean

# Виведення результатів
print(f"Рівняння лінії: y = {a:.2f}x + {b:.2f}")

# Побудова графіка
plt.scatter(x, y, color='red', label='Точки даних')
plt.plot(x, a * x + b, color='blue', label='Лінія найкращої підгонки')

plt.xlabel('x')
plt.ylabel('y')
plt.title('МНК. Наближення прямою')
plt.legend()
plt.grid(True)
plt.show()
