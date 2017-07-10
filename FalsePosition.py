# John Berkley
# CS 301
# 7/8/2017

from math import cosh, fabs


def false_position(func, a, b, e, true_value):
    fa = func(a)
    fb = func(b)
    c = a + b / 2

    for n in range(100):
        prev_c = c
        c = b - ((fb * (b - a)) / (fb - fa))
        fc = func(c)
        rel_error = fabs((c - prev_c) / c)
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, c, fc))
        print('\tRelative Error: {} ; True Error: {}'.format(rel_error, (fabs(true_value - c) / true_value)))
        if abs(rel_error) < e:
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


false_position(f, 0, 1, .01, 0.3651)
false_position(f, 1, 2, .01, 1.92174)
false_position(f, 3, 4, .01, 3.56316)

false_position(g, 120, 130, .01, 126.632)
