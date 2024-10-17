from scipy import integrate
import numpy as np

# завдання 1 (метод прямокутників)
# межі інтегралу
print('Завдання 1')
a = 2
b = 3.5
n = 10
h = (b - a) / n  # Крок

def f1(x):
    return 1 / np.sqrt(x - 1)   # Функція для інтегрування

def left_rec(f1, a, b, n, h):    # Метод лівих прямокутників
    total = 0
    for i in range(0, n):
        total += f1(a + i * h)
    return total * h

def right_rec(f1, a, b, n, h):   # Метод правих прямокутників
    total = 0
    for i in range(1, n + 1):
        total += f1(a + i * h)
    return total * h

def aver_rec(f1, a, b, n, h):    # Метод середніх прямокутників
    total = 0
    for i in range(0, n):
        total += f1(a + (i + 0.5) * h)
    return total * h

# Виведення результатів
print("Лівий прямокутник:", round(left_rec(f1, a, b, n, h), 4))
print("Правий прямокутник:", round(right_rec(f1, a, b, n, h), 4))
print("Середній прямокутник:", round(aver_rec(f1, a, b, n, h), 4))

v, err = integrate.quad(f1, a, b)      # Перевірка за допомогою функції scipy
print("Check with SciPy quad method:", round(v, 4))



# завдання 2 (метод Сімпсона)
print('Завдання 2')
def f(x):    # Задаємо функцію, яку необхідно інтегрувати
    return np.sin(x) / (x + 1)   

# межі інтегралу
a = 0.18  
b = 0.98
n = 8

def simpson_rule(f, a, b, n):    # Обчислюємо значення інтегралу методом Симпсона
    h = (b - a) / n  # Ініціалізація h всередині функції
    integr = f(a) + f(b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integr += 2 * f(k)
        else:
            integr += 4 * f(k)
    integr *= h / 3  # Правильне розміщення множення на h/3
    return integr

# виводимо результат
print("метод Симпсона:", round(simpson_rule(f, a, b, n), 4))

v, err = integrate.quad(f, a, b) 
print("Check for the Simpson method =", round(v, 4))    # перевірка



#завдання 3  (метод трапецій)
print('Завдання 3')

def f(x):   # задаємо функцію, яку необхідно інтегрувати
    return 1 / (0.5 * x**2 + 1)**0.5  

# задаємо межі інтегрування та кількість розбиттів (n)
a = 3.2
b = 4
n = 20  


def trapezoidal_rule(f, a, b, n):    # обчислюємо значення інтегралу методом трапецій
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    x = a
    for i in range(1, n):  # проходимо по всіх інтервалах
        x += h
        sum += f(x)
    integral = h * sum
    return integral

integral = trapezoidal_rule(f, a, b, n)    # Виводимо результат методу трапецій
print("Результат методу трапецій:", round(integral, 4))

v, err = integrate.quad(f, a, b)    # Перевірка
print("Перевірка за допомогою методу SciPy quad:", round(v, 4))