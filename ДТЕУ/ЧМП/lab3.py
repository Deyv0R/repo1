from sympy import symbols, diff

x = symbols('x')

# Завдання 1 метод Ньютона
f1_expr = 3 * x**4 + 2 * x**3 + x**2 + x - 5

def newton(a, b, eps):
    f1_prime = diff(f1_expr, x)  # Перша похідна
    f1_double_prime = diff(f1_prime, x)  # Друга похідна
    
    if f1_expr.subs(x, b) * f1_double_prime.subs(x, b) > 0:
        xi = b
    else:
        xi = a
    while True:
        df = f1_prime.subs(x, xi)  
        xi_1 = xi - f1_expr.subs(x, xi) / df  # Формула методу Ньютона
        if abs(xi_1 - xi) < eps:  # Перевірка точності
            break
        xi = xi_1
    return print("Розв'язання рівняння методом Ньютона x = ", xi_1)

newton(-2.0, -1/2, 0.0001) # Метод Ньютона з початковими значеннями

# Завдання 2 комбінований метод
def komb(a, b, eps):
    f2_expr = f1_expr
    f2_prime = diff(f2_expr, x)  # Перша похідна

    if f2_prime.subs(x, a) * diff(f2_prime, x).subs(x, a) > 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai - bi) > eps: # Основний цикл комбінованого методу
        ai_1 = ai - f2_expr.subs(x, ai) * (bi - ai) / (f2_expr.subs(x, bi) - f2_expr.subs(x, ai))
        bi_1 = bi - f2_expr.subs(x, bi) / f2_prime.subs(x, bi)
        ai = ai_1
        bi = bi_1
    x_res = (ai + bi) / 2 # Середнє значення між ai та bi
    return print("Розв'язання рівняння комбінованим методом x =", x_res)

komb(-2, -1/2, 0.0001) # Комбінований метод з початковими значеннями
