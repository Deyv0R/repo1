import numpy as np
import matplotlib.pyplot as plt

# визначення значень функції x і y
x_values = np.array([3.2, 3.3, 3.4, 3.5, 3.6, 3.7])   # аргументи функції
y_values = np.array([3.983, 4.070, 4.155, 4.237, 4.319, 4.400])   # значення функції

h = x_values[1] - x_values[0]    # крок таблиці

def finite_differences(y):    # обчислення кінцевих різниць
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:, 0] = y
    for j in range(1, n):  
        for i in range(n - j):   
            delta_y[i, j] = delta_y[i + 1, j - 1] - delta_y[i, j - 1] 
    return delta_y

delta_table = finite_differences(y_values)   # отримуємо таблицю кінцевих різниць

# виведення таблиці кінцевих різниць
print("Таблиця кінцевих різниць:")
np.set_printoptions(precision=4, suppress=True)
print(delta_table)

# Значення кінцевих різниць для першої та другої похідних
delta_y1 = delta_table[0, 1]  # Δy1
delta2_y1 = delta_table[0, 2]  # Δ²y1
delta3_y1 = delta_table[0, 3]  # Δ³y1
delta4_y1 = delta_table[0, 4]  # Δ⁴y1

def first_derivative(delta_y1, delta2_y1, delta3_y1, delta4_y1, h):     # функція для обчислення першої похідної за формулою Ньютона
    return (delta_y1 - delta2_y1 / 2 + delta3_y1 / 3 - delta4_y1 / 4) / h

def second_derivative(delta2_y1, delta3_y1, delta4_y1, h):    # функція для обчислення другої похідної за формулою Ньютона
    return (delta2_y1 - delta3_y1 + 11 * delta4_y1 / 12) / h**2

# обчислюємо першу та другу похідні в точці x = 3.4
y1_prime = first_derivative(delta_y1, delta2_y1, delta3_y1, delta4_y1, h)
y1_double_prime = second_derivative(delta2_y1, delta3_y1, delta4_y1, h)

# результат похідних
print(f"Перша похідна при x = 3.4: {y1_prime:.3f}")
print(f"Друга похідна при x = 3.4: {y1_double_prime:.3f}")


# графік функції
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Функція y = f(x)', marker='o', color='b')
plt.title('Графік функції y = f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# графік першої похідної (лінійна апроксимація)
plt.figure(figsize=(10, 6))
plt.plot([x_values[2], x_values[2]], [0, y1_prime], label="Перша похідна", marker='o', color='r')
plt.title("Перша похідна функції")
plt.xlabel("x")
plt.ylabel("y'")
plt.grid(True)
plt.legend()
plt.show()

# графік другої похідної (лінійна апроксимація)
plt.figure(figsize=(10, 6))
plt.plot([x_values[2], x_values[2]], [0, y1_double_prime], label="Друга похідна", marker='o', color='g')
plt.title("Друга похідна функції")
plt.xlabel("x")
plt.ylabel("y''")
plt.grid(True)
plt.legend()
plt.show()
