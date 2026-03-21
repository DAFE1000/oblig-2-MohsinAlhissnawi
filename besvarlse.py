from math import atan, exp

# Funksjonen f(x)
def f(x):
    return exp(-x/4) * atan(x)

# Likningen som bestemmer maksimumspunktet
def g(x):
    return atan(x) - 4/(1 + x**2)

# Derivert av g(x) for Newtons metode
def g_prime(x):
    return 1/(1+x**2) + 8*x/(1+x**2)**2

# Newtons metode
def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Startverdi
x_start = 1.5

# Finn maksimumspunktet
x_max = newton(g, g_prime, x_start)
y_max = f(x_max)

print("Maksimumspunkt:")
print(f"x = {x_max:.6f}")
print(f"f(x) = {y_max:.6f}")