# John Berkley
# CS 301
# 7/8/2017


from math import fabs, cosh


def bisection(func, a, b, e, true_value):
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
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, c, fc))
        print('\tRelative Error: {} ; True Error: {}'.format(error, (fabs(true_value - c) / true_value)))
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


bisection(f, 0, 1, .01, 0.3651)
bisection(f, 1, 2, .01, 1.92174)
bisection(f, 3, 4, .01, 3.56316)

bisection(g, 120, 130, .01, 126.632)
