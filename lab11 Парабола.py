import numpy as np
import matplotlib.pyplot as plt

# Визначення функції для генерації y
def func(xi):
    return xi**2 * np.sin(xi)

x = np.array([i * 0.1 for i in range(0, 9)])  
y = np.array([func(xi) for xi in x])

print('x=', x)
print('y=', y)

# Використання polyfit для знаходження коефіцієнтів полінома другого порядку (ступінь 2)
coefficients = np.polyfit(x, y, 2)

# Виведення результатів
a, b, c = coefficients  
print(f"Рівняння параболи: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")

# Створення поліноміальної функції для отриманих коефіцієнтів
polynomial = np.poly1d(coefficients)

# Побудова графіка
plt.scatter(x, y, color='red', label='Точки даних', s=10)
x_line = np.linspace(min(x), max(x), 100)
plt.plot(x_line, polynomial(x_line), color='blue', label='Апроксимація поліномом')

plt.title('Поліном другого порядку МНК за допомогою polyfit()')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
