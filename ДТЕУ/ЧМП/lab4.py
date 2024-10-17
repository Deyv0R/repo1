import numpy as np

# Задаємо матрицю 3*3
m_sqr_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(m_sqr_arr)

# Ще один варіант як задати матрицю
m_sqr_mx = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(m_sqr_mx)

# Побудуємо діагональ
m_sqr_mx = np.matrix('1 2 3; 4 5 6; 7 8 9')
diag = np.diag(np.array(m_sqr_mx))
print(diag)

# Побудуємо діагональну матрицю на базі полученої діагоналі
m_diag_np = np.diag(diag)
print(m_diag_np)

# Транспонована матриця
a = np.matrix('1 2 3; 4 5 6')
print('A=', a)
a_t = a.transpose()
print(a_t)
print(a.T) # ще один спосіб транспонування матриці

# Визначник матриці
a = np.matrix('1 2; 3 4')
a_det = np.linalg.det(a)
print(format(a_det, '.9g'))

# Множення матриці на число
a = np.matrix('1 2 3; 4 5 6')
c = 3 * a
print(c)

# Додавання матриць
a = np.matrix('1 6 3; 8 2 7')
b = np.matrix('8 1 5; 6 9 12')
c = a + b
print(c)

# Добуток матриць
a = np.matrix('1 2 3; 4 5 6')
b = np.matrix('7 8; 9 1; 2 3')
c = a.dot(b)
print(c)

# Обернена матриця
A = np.matrix('1 -3; 2 5')
A_inv = np.linalg.inv(A)
print(A_inv)

# Ранг матриці
rank = np.linalg.matrix_rank(A)
print(rank)

# Матричний метод
A = np.matrix('3 -1 2; 1 4 -1; 2 3 1')
B = np.matrix('-4; 10; 8')
print('A=', A)
print('B=', B)
A_inv = np.linalg.inv(A)
print(A_inv)
X = A_inv.dot(B)
print('X=', X)

# Метод Крамера
a = np.matrix('3 -1 2; 1 4 -1; 2 3 1')
print('A=', a)
b = np.matrix('-4; 10; 8')
print('B=', b)

def kramer(a, b):
    a_det = np.linalg.det(a)
    print('Детермінант матриці = ', a_det)
    # Перевірка, що детермінант не дорівнює нулю
    if a_det != 0:
        print('Розв*язуємо систему')
        x_m = np.matrix(a)
        x_m[:, 0] = b  # формування допоміжної матриці (1 ст. замінюємо на ст. b)
        print('x_m=', x_m)
        y_m = np.matrix(a)  # 2 ст. замінюємо на ст. b
        y_m[:, 1] = b
        print('y_m=', y_m)
        z_m = np.matrix(a)  # 3 ст. замінюємо на ст. b
        z_m[:, 2] = b
        print('z_m=', z_m)
        x = np.linalg.det(x_m) / a_det
        y = np.linalg.det(y_m) / a_det
        z = np.linalg.det(z_m) / a_det
        print('X = ', round(x, 5))
        print('Y=', round(y, 5))
        print('Z=', round(z, 5))
    else:
        print('Розв*язків немає')

kramer(a, b)

# Перевірка за допомогою методу solve() пакету linalg:
X = np.linalg.solve(a, b)
print('Перевірка X=', X)

# Розв’язання системи методом Гауса
a = np.matrix('1 1 1; 0 1 -1; 1 0 -1', dtype=float)
b = np.matrix('1500; 140; 80', dtype=float)

# Виводимо початкову систему
print("Початкова система:")
print(a)
print(b)

# Застосовуємо метод Гауса
n = b.shape[0]
x = np.zeros(n)

# Прямий хід
for k in range(n-1):
    for i in range(k+1, n):
        factor = a[i,k] / a[k,k]
        for j in range(k, n):
            a[i,j] = a[i,j] - factor * a[k,j]
        b[i] = b[i] - factor * b[k]

# Зворотній хід
x[n-1] = b[n-1] / a[n-1,n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0
    for j in range(i+1, n):
        sum_ax += a[i,j] * x[j]
    x[i] = (b[i] - sum_ax) / a[i,i]

# Виводимо розв'язок
print("Розв'язок:")
print(x.round(3))
print('Перевірка рішення за допомогою np.linalg.solve:\n', np.linalg.solve(a, b).round(3))
