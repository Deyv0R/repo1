import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Функція, що повертає dy/dx
def model(y, x):
    return np.sin(y / np.sqrt(5))

# Початкова умова
Y0 = 2.6

# Значення x
x = np.arange(1.8, 2.8, 0.1)

# Розв'язання ODE
y = odeint(model, Y0, x)

# Виведення результатів
print('x=', x)
print('y=', y.flatten())  # Перетворення в одновимірний масив для виводу

# Побудова графіка результатів
plt.plot(x, y, marker='o')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Розв’язання диф. рівняння y\' = x + sin(y / sqrt(5))')
plt.grid()
plt.show()
