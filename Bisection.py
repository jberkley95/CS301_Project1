from math import fabs, cosh


def bisection(func, a, b, e):
    fa = func(a)
    fb = func(b)
    if not fa * fb < 0:
        print('{} : {}'.format(fa, fb))
        print('\nBracketing Condition Failed\n')
        return
    error = b - a
    for n in range(100):
        error /= 2
        c = a + error
        fc = func(c)
        print('{} : {} : {} : {}'.format(n, c, fc, error))
        if abs(error) < e:
            print('\nConverged to Root\n')
            return
        if fb * fc < 0:
            a = c
            fa = fc
        else:
            b = c
            fb = fc


def f(x):
    return (2 * (x ** 3)) - (11.7 * (x ** 2)) + (17.7 * x) - 5


def g(x):
    return x + 10 - (x * cosh(50 / x))


bisection(f, 0, 1, .01)
bisection(g, 120, 130, .01)
