def calculate_polynomial(n, coefficients, x):
    y = 0 
    for i in range(n + 1):
        y += coefficients[i] * (x ** i)
    return y

n = int(input("Кількість коефіцієнтів n: "))
coefficients = []
for i in range(n + 1):
    coefficient = float(input(f"Коефіцієнт a_{i}: "))
    coefficients.append(coefficient)

x = float(input("Значення x: "))

result = calculate_polynomial(n, coefficients, x)

print(f"Результат: y = {result}")
