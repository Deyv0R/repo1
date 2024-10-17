import numpy as np

# таблиця значень функції (задаємо значення x і y)
x_values = np.array([3.2, 3.3, 3.4, 3.5, 3.6, 3.7])   # аргументи функції
y_values = np.array([3.983, 4.070, 4.155, 4.237, 4.319, 4.400])   # значення функції

h = x_values[1] - x_values[0]   # крок таблиці

def finite_differences(y):    # обчислення кінцевих різниць
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            delta_y[i, j] = delta_y[i + 1, j - 1] - delta_y[i, j - 1]
    return delta_y

delta_table = finite_differences(y_values)   # отримуємо таблицю кінцевих різниць

# Виводимо таблицю кінцевих різниць 
print("Таблиця кінцевих різниць:")
np.set_printoptions(precision=4, suppress=True)
print(delta_table)

# Значення кінцевих різниць для першої та другої похідних
delta_y1 = delta_table[1, 1]  # Δy1
delta2_y1 = delta_table[1, 2]  # Δ²y1
delta3_y1 = delta_table[1, 3]  # Δ³y1
delta4_y1 = delta_table[1, 4]  # Δ⁴y1

def first_derivative(delta_y1, delta2_y1, delta3_y1, delta4_y1, h):    # Функція для обчислення першої похідної за формулою Ньютона
    return (delta_y1 - delta2_y1 / 2 + delta3_y1 / 3 - delta4_y1 / 4) / h

def second_derivative(delta2_y1, delta3_y1, delta4_y1, h):   # Функція для обчислення другої похідної за формулою Ньютона
    return (delta2_y1 - delta3_y1 + 11 * delta4_y1 / 12) / h**2

# обчислюємо першу та другу похідні в точці x = 3.4
y1_prime = first_derivative(delta_y1, delta2_y1, delta3_y1, delta4_y1, h)
y1_double_prime = second_derivative(delta2_y1, delta3_y1, delta4_y1, h)

y1_prime = round(y1_prime, 3)
y1_double_prime = round(y1_double_prime, 3)

# результати
print(f"\nПерша похідна y'(3.4) ≈ {y1_prime}")
print(f"Друга похідна y''(3.4) ≈ {y1_double_prime}")