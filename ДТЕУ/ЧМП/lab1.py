import numpy as np

#завдання 1
x1 = 21
x1_1 = 4.58
x2 = 21/29
x2_1 = 0.724

print('Завдання 1')

def f(x, y): # функція f, яка приймає аргументи x і y
    return np.abs(x - y) / np.abs(x)

# обчислення відносної похибки для першої і другої пари значень
rel_error_x1 = f(x1, x1_1)
rel_error_x2 = f(x2, x2_1)

# виведення результатів
if rel_error_x1 < rel_error_x2:
    print('перша рівність точніша:', round(rel_error_x1, 5))
elif rel_error_x2 < rel_error_x1:
    print('друга рівність точніша:', round(rel_error_x2, 5))
else:
    print('Обидві рівності мають однакову точність:', round(rel_error_x2, 5))


#завдання 2
print('Завдання 2')

def round_narrow(value, uncertainty):
    #Округлення в вузькому розумінні
    decimal_places = abs(int(np.floor(np.log10(uncertainty))))
    rounded_value = np.round(value, decimal_places)
    return rounded_value

def round_wide(value, uncertainty):
    #Округлення в широкому розумінні
    sig_figs = int(np.ceil(-np.log10(uncertainty))) + 1
    rounded_value = np.round(value, sig_figs)
    rounded_uncertainty = np.round(uncertainty, sig_figs)
    return rounded_value, rounded_uncertainty

# Приклад а
num_a = 13.6253
num_a_1 = 0.0021

narrow_a = round_narrow(num_a, num_a_1)
print(f"Вузьке розуміння a: {narrow_a}")
wide_a, wide_uncertainty_a = round_wide(num_a, num_a_1)
print(f"Широке розуміння a: {wide_a} ± {wide_uncertainty_a}")

# Приклад б
num_b = 0.3567
num_b_1 = 0.3567 * 0.00042  # δ = 0.042%

narrow_b = round_narrow(num_b, num_b_1)
print(f"Вузьке розуміння b: {narrow_b}")
wide_b, wide_uncertainty_b = round_wide(num_b, num_b_1)
print(f"Широке розуміння b: {wide_b} ± {wide_uncertainty_b}")


#завдання 3
print('Завдання 3')

def calculate_errors(value):
    #розрахунок похибок у вузькому розумінні
    narrow_absolute_error = 10 ** (-len(str(value).split('.')[1]))
    narrow_relative_error = narrow_absolute_error / value

    # У широкому розумінні
    sig_figs = len(str(value).replace('.', '').strip('0'))
    wide_absolute_error = narrow_absolute_error
    wide_relative_error = wide_absolute_error / value

    return narrow_absolute_error, narrow_relative_error, wide_absolute_error, wide_relative_error

# виведення результатів
value_a = 3.751
narrow_absolute_a, narrow_relative_a, wide_absolute_a, wide_relative_a = calculate_errors(value_a)
print(f"Число: {value_a}")
print(f"Вузьке розуміння: Абсолютна похибка = {narrow_absolute_a}, Відносна похибка = {narrow_relative_a * 100}%")
print(f"Широке розуміння: Абсолютна похибка = {wide_absolute_a}, Відносна похибка = {wide_relative_a * 100}%")

value_b = 0.537
narrow_absolute_b, narrow_relative_b, wide_absolute_b, wide_relative_b = calculate_errors(value_b)
print(f"\nЧисло: {value_b}")
print(f"Вузьке розуміння: Абсолютна похибка = {narrow_absolute_b}, Відносна похибка = {narrow_relative_b * 100}%")
print(f"Широке розуміння: Абсолютна похибка = {wide_absolute_b}, Відносна похибка = {wide_relative_b * 100}%")
