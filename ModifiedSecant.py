# John Berkley
# CS 301
# 7/8/2017

from math import cosh, fabs


def modified_secant(func, x1, delta, e, true_value):
    for n in range(100):
        x2 = x1 - f(x1) * ((delta * x1) / (f(x1 + (delta * x1)) - f(x1)))
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, x2, func(x2)))
        print('\tRelative Error: {} ; True Error: {}'.format(fabs((x2 - x1) / x2), (fabs(true_value - x2) / true_value)))
        if fabs((x2 - x1) / x2) < e:
            print('\nConverged To Root\n')
            return
        else:
            x1 = x2


def f(x):
    return (2 * (x ** 3)) - (11.7 * (x ** 2)) + (17.7 * x) - 5


def g(x):
    return x + 10 - (x * cosh(50 / x))


modified_secant(f, .5, .01, .01, 0.3651)
modified_secant(f, 2, .01, .01, 1.92174)
modified_secant(f, 3, .01, .01, 3.56316)

modified_secant(g, 120, .01, .01, 126.632)