import numpy as np
import matplotlib.pyplot as plt

# задані точки
x = np.arange(1.415, 1.470, 0.005)
y = np.array([0.8885, 0.8895, 0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976, 0.8986])

# перша інтерполяційна формула
def first_interpolation(x, y, x0):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y  # заповнення перших стовпців значеннями y
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    ans = 0
    for j in range(n):
        prod = f[0][j]
        for i in range(j):
            prod *= (x0 - x[i])
        ans += prod
    return ans

# друга інтерполяційна формула 
def second_interpolation(x, y, x0):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y  # заповнення перших стовпців значеннями y
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    ans = f[0][0]
    for j in range(1, n):
        prod = f[0][j]
        for i in range(j):
            prod *= (x0 - x[i])
        ans += prod
    return ans

# Значення аргумента x для обчислень
x_values_to_interpolate = np.array([1.416, 1.456, 1.431, 1.462, 1.422, 1.451])

# обчислюємо значення функції в заданих точках
for x0 in x_values_to_interpolate:
    y_interpolated = first_interpolation(x, y, x0)
    print(f"f({x0}) = {y_interpolated}")

# будуємо графік інтерполяційної функції
xx = np.linspace(1.410, 1.470, 100)  # 100 точок між 1.410 та 1.470
yy = np.zeros_like(xx)  # масив для значень інтерполяційної функції
for i in range(len(xx)):
    yy[i] = second_interpolation(x, y, xx[i])

plt.plot(x, y, 'o', label='Дані точки', color='red')  # дані точки
plt.plot(xx, yy, label='Інтерполяційна функція', color='blue')  # інтерполяційна функція
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Інтерполяція Лагранжа')
plt.legend()
plt.show()
