import numpy as np

# Завдання 1        №1
print('Завдання 1     №1')
A = np.array([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
B = np.array([[1, 2, 1], [0, 1, 2], [3, 1, 1]])

AB = np.dot(A, B)
BA = np.dot(B, A)

result = AB - BA
print("AB - BA = \n", result)

# №2
print('№ 2')
Ax = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
A_squared = np.dot(Ax, Ax)

print("A^2 = \n", A_squared)

# №3
print('№ 3')
A1 = np.array([[3, 5], [6, -1]])
B1 = np.array([[2, 1], [-3, 2]])
C1 = np.dot(A1, B1)

print("Добуток A і B = \n", C1)

# №4
print('№ 4')
A2 = np.array([[2, 3, 4], [1, 0, 6], [7, 8, 9]])
det_A2 = np.linalg.det(A2)

print("Визначник матриці A = ", det_A2)

# №5
print('№ 5')
A3 = np.array([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
det_A3 = np.linalg.det(A3)

print("Визначник матриці A = ", det_A3)

# №6
print('№ 6')
A4 = np.array([[1, 2, -3], [0, 1, 2], [0, 0, 1]])
A4_inv = np.linalg.inv(A4)

print("Обернена матриця A = \n", A4_inv)

# №7
print('№ 7')
A5 = np.array([[1, -1, 3, 4], [0, -1, 2, 1], [1, 1, -1, 2], [2, 3, -5, 3]])
rank_A = np.linalg.matrix_rank(A5)

print("Ранг матриці A = ", rank_A)

# №8
# Матричний метод
print('№ 8')
A6 = np.matrix('2 -1 1; 3 4 -2; 1 -3 1')
B6 = np.matrix('5; -3; 4')
print('A=', A6)
print('B=',B6)
A6_inv = np.linalg.inv(A6)
print(A6_inv)
X = A6_inv.dot(B6)
print('X=',X)

# Метод Крамера
a = np.matrix('2 -1 1; 3 4 -2; 1 -3 1')
print('A=',a)
b = np.matrix('5; -3; 4')
print('B=',b)
def kramer (a, b):
 a_det = np.linalg.det(A)
 print('Детермінант матриці = ', a_det)
 if (a_det != 0):
  print ('Розв*язання системи')

  x_m = np.matrix(a)
  x_m[:, 0] = b
  print('x_m=', x_m)

  y_m = np.matrix(a)
  y_m[:, 1] = b
  print('y_m=',y_m)

  z_m = np.matrix(a)
  z_m[:, 2] = b
  print('z_m=',z_m)

  x = np.linalg.det(x_m) / a_det
  y = np.linalg.det(y_m) / a_det
  z = np.linalg.det(z_m) / a_det

  print('X = ', round(x,5))
  print('Y=', round(y,5))
  print('Z=', round(z,5))

kramer(a,b)
X = np.linalg.solve(a, b)
print('Перевірка X=',X)

# Метод Гауса
a1 = np.array([[2, -1, 1],
              [3, 4, -2],
              [1, -3, 1]], dtype=float)

b1 = np.array([5, -3, 4], dtype=float)

print("Початкова система:")
print("A:")
print(a1)
print("B:")
print(b1)

n = len(B)
for k in range(n-1):
    for i in range(k+1, n):
        factor = a1[i, k] / a1[k, k]
        a1[i, k:] -= factor * a1[k, k:]
        b1[i] -= factor * b1[k]

x1 = np.zeros(n)
x1[n-1] = b1[n-1] / a1[n-1, n-1]

for i in range(n-2, -1, -1):
    sum_ax = np.sum(a1[i, i+1:] * x1[i+1:])
    x1[i] = (b1[i] - sum_ax) / a1[i, i]

print("Розв'язок:")
print(x1.round(5))


# Завдання 2      №5
print('Завдання 2     №5')
N = 4
M = 5
A7 = np.array([[np.random.randint(1, 10) for _ in range(M)] for _ in range(N)])
print("Матриця A:\n", A7)

total_sum = 0
for row in A7:
    total_sum += sum(row)

print("\nСума всіх елементів матриці A:", total_sum)

row_sums = []
for row in A7:
    row_sums.append(sum(row))

print("\nСума елементів кожного рядка:", row_sums)

row_shares = []
for row_sum in row_sums:
    row_shares.append(row_sum / total_sum)

print("Частка кожного рядка від загальної суми:")
for i in range(N):
    print("Рядок", i+1, ":", round(row_shares[i], 4))
