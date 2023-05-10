import math

def f(x):
    return x**3 + x + 16

def bisection(a, b, tol):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        return "No hay cambio de signo en el intervalo. No se puede aplicar el método de la bisección."
    c = (a+b)/2
    fc = f(c)
    i = 0
    while abs(fc) > tol:
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        c = (a+b)/2
        fc = f(c)
        i += 1
    return c, i

def secant(x0, x1, tol):
    i = 0
    while abs(f(x1)) > tol:
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        x0 = x1
        x1 = x2
        i += 1
    return x1, i

def newton_raphson(x0, tol):
    i = 0
    while abs(f(x0)) > tol:
        df = (f(x0 + tol) - f(x0))/tol  # aproximación de la derivada
        x1 = x0 - f(x0)/df
        x0 = x1
        i += 1
    return x1, i

a = -10
b = 10
tol = 1e-6

sol_bisection, iter_bisection = bisection(a, b, tol)
sol_secant, iter_secant = secant(a, b, tol)
sol_newton, iter_newton = newton_raphson(a, tol)

print("MÉTODO\t\tCANTIDAD DE ITERACIONES\tSOLUCIÓN")
print("Bisección:\t{}\t\t\t{}".format(iter_bisection, sol_bisection))
print("Secante:\t{}\t\t\t{}".format(iter_secant, sol_secant))
print("Newton-Raphson:\t{}\t\t\t{}".format(iter_newton, sol_newton))
