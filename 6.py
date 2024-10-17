import numpy as np
import matplotlib.pyplot as plt

# Функція для обчислення інтерполяційного багаточлена Лагранжа
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Задані точки
x_values = [-2, -1, 0, 1]
y_values = [-7, 4, 1, 2]

# Точки для обчислення наближених значень
x_points = [-0.5, 1.5, 2, 2.5]

# Обчислення наближених значень і збереження їх у y_points
y_points = [lagrange_interpolation(x_values, y_values, x) for x in x_points]

# Виведення результатів
for x, y in zip(x_points, y_points):
    print(f"L({x}) = {y:.3f}")

# Побудова графіка
x_plot = np.linspace(-3, 3, 500)
y_plot = [lagrange_interpolation(x_values, y_values, x) for x in x_plot]

plt.plot(x_plot, y_plot, label="Ln(x) - Lagrange Interpolation")
plt.scatter(x_values, y_values, color='red', label="Given points")
plt.scatter(x_points, y_points, color='blue', label="Approximated points")
plt.legend()
plt.title("Lagrange Interpolation Polynomial")
plt.xlabel("x")
plt.ylabel("Ln(x)")
plt.grid(True)
plt.show()

# Перевірка
xnew = np.linspace(min(x_values), max(x_values), 500)
ynew = [lagrange_interpolation(x_values, y_values, x) for x in xnew]

# Побудова перевірочного графіка
fig = plt.figure(figsize=(10, 8))
plt.plot(xnew, ynew, 'b', x_values, y_values, 'ro')  # 'b' - синя лінія для інтерполяції, 'ro' - червоні точки
plt.title('Lagrange Polynomial - Verification')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Додаткова перевірка з використанням інтерполяційної функції
f = lambda x: lagrange_interpolation(x_values, y_values, x)
fig = plt.figure(figsize=(10, 8))
plt.plot(xnew, [f(x) for x in xnew], 'b', x_values, y_values, 'ro')
plt.title('Lagrange Polynomial_2 - Additional Verification')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
