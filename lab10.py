import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# Задаємо символьну змінну x та функцію f(x)
x = sp.symbols('x')
f = x**2 * sp.sin(2*x)

# Знаходимо чотири похідні
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)
f3 = sp.diff(f2, x)
f4 = sp.diff(f3, x)  

# Виводимо похідні
print("f'(x) =", f1)
print("f''(x) =", f2)
print("f'''(x) =", f3)
print("f''''(x) =", f4)

# Знаходимо значення функції та її похідних в точці x=0
x0 = 0
f_x0 = f.subs(x, x0).evalf()
f1_x0 = f1.subs(x, x0).evalf()
f2_x0 = f2.subs(x, x0).evalf()
f3_x0 = f3.subs(x, x0).evalf()

# Обчислюємо значення полінома Тейлора в точці x=0
T = f_x0 + f1_x0*(x-x0) + (f2_x0/2)*(x-x0)**2 + (f3_x0/6)*(x-x0)**3
print("f(0) =", f_x0)
print("T(x) =", T)

# Оцінюємо максимальну похибку для полінома Тейлора третього степеня
x_vals_sym = np.linspace(-1, 1, 1000)
f4_vals = np.array([f4.subs(x, xi).evalf() for xi in x_vals_sym])
max_f4 = np.max(np.abs(f4_vals))  # Максимальне значення четвертої похідної на відрізку

# Оцінка похибки
error_estimation = max_f4 * (1 - x0)**4 / 24  # Оцінка похибки, залишковий член
print(f"Оцінка похибки Тейлора третього степеня: {error_estimation}")

# Будуємо графіки функції та полінома Тейлора
x_vals = np.linspace(-2, 2, 1000)
f_vals = np.array([f.subs(x, xi).evalf() for xi in x_vals])
T_vals = np.array([T.subs(x, xi).evalf() for xi in x_vals])

fig, ax = plt.subplots()
ax.plot(x_vals, f_vals, label="f(x) = x^2 * sin(2x)", color='blue')
ax.plot(x_vals, T_vals, label="Тейлор (3rd order)", color='red', linestyle='--')
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Графік функції та наближення поліномом Тейлора")
plt.grid(True)
plt.show()

# Побудова графіку похибки між функцією та поліномом Тейлора
error_vals = np.abs(f_vals - T_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, error_vals, label='Похибка', color='green')
ax.set_xlabel("x")
ax.set_ylabel("Похибка")
ax.set_title("Оцінка похибки між f(x) і поліномом Тейлора")
plt.grid(True)
plt.show()

# Побудова полінома Тейлора за допомогою scipy
def f_numeric(x):
    return x**2 * np.sin(2*x)

x_scipy = np.linspace(-2.0, 2.0, num=400)
degree = 3
taylor = approximate_taylor_polynomial(f_numeric, 0, degree, 1)

plt.figure(figsize=(10, 6))
plt.plot(x_scipy, f_numeric(x_scipy), label="f(x) curve", color='blue')
plt.plot(x_scipy, taylor(x_scipy), label=f"degree={degree}", color='red', linestyle='--')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, shadow=True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення поліномом Тейлора за допомогою scipy")
plt.tight_layout()
plt.grid()
plt.show()
