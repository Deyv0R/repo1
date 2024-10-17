import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):    # функція для обчислення інтерполяційного багаточлена Лагранжа
    n = len(x_values)
    result = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term  
    return result

# задані точки для інтерполяції
x_values = [-2, -1, 0, 1]
y_values = [-7, 4, 1, 2]

x_points = [-0.5, 1.5, 2, 2.5]
y_points = [lagrange_interpolation(x_values, y_values, x) for x in x_points]   # обчислення наближених значень за допомогою функції Лагранжа


for x, y in zip(x_points, y_points):   # виведення результатів
    print(f"L({x}) = {y:.3f}")

# побудова графіка
x_plot = np.linspace(-3, 3, 500)
y_plot = [lagrange_interpolation(x_values, y_values, x) for x in x_plot]    # обчислення значення функції для кожної точки

plt.plot(x_plot, y_plot, label="Ln(x) - Lagrange Interpolation")
plt.scatter(x_values, y_values, color='red', label="Given points")
plt.scatter(x_points, y_points, color='blue', label="Approximated points")
plt.legend()
plt.title("Lagrange Interpolation Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# перевірка
xnew = np.linspace(min(x_values), max(x_values), 500)
ynew = [lagrange_interpolation(x_values, y_values, x) for x in xnew]

# побудова перевірочного графіка
fig = plt.figure(figsize=(10, 8))
plt.plot(xnew, ynew, 'b', x_values, y_values, 'ro')    # 'b' - синя лінія, 'ro' - червоні точки
plt.title('Lagrange Polynomial - Verification')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
