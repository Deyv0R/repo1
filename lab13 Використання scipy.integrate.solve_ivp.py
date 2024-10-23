import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Функція, що повертає dy/dx
def model(x1, y1):
    return x1 + np.cos(y1 / 3)

# Початкова умова
y0 = [4.6]  # Потрібно передати як список

# Значення x
x1 = np.linspace(1.6, 2.6, 6)

# Розв'язання ODE
sol = solve_ivp(model, [1.6, 2.6], y0, t_eval=x1)

# Виведення результатів
print('x=', sol.t)
print('y=', sol.y[0])

# Побудова графіка результатів
plt.plot(sol.t, sol.y[0], marker='o')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Розв’язання диф. рівняння')
plt.grid()
plt.show()