# John Berkley
# CS 301
# 7/8/2017

import xlsxwriter
from math import fabs, cosh

book = xlsxwriter.Workbook('newton.xls')
sheet1 = book.add_worksheet()
sheet1.write(0, 0, "Procedure Name")
sheet1.write(0, 1, "Iteration")
sheet1.write(0, 2, "Current Value")
sheet1.write(0, 3, "Function Value")
sheet1.write(0, 4, "Relative Error")
sheet1.write(0, 5, "True Error")


def newton(func, dfunc, x, e, true_value, xls_initial_row, procedure_name):
    fx = func(x)

    for n in range(100):
        prev_x = x
        fp = dfunc(x)
        d = fx / fp
        x -= d
        fx = func(x)
        rel_error = fabs((x - prev_x) / x)
        true_error = fabs(true_value - x) / true_value
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, x, fx))
        print('\tRelative Error: {} ; True Error: {}'.format(rel_error, true_error))
        if n == 0:
            sheet1.write(xls_initial_row + n, 0, procedure_name)
        sheet1.write(xls_initial_row + n, 1, n)
        sheet1.write(xls_initial_row + n, 2, x)
        sheet1.write(xls_initial_row + n, 3, fx)
        sheet1.write(xls_initial_row + n, 4, rel_error)
        sheet1.write(xls_initial_row + n, 5, true_error)
        if rel_error < e:
            print('\nConverged To Root\n')
            return xls_initial_row + n + 2


def f(x):
    return (2 * (x ** 3)) - (11.7 * (x ** 2)) + (17.7 * x) - 5


def df(x):
    return (6 * (x ** 2)) - (23.4 * x) + 17.7


def g(x):
    return x + 10 - (x * cosh(50 / x))


def dg(x):
    return 1 - (((cosh(50 / x) * x) - (50 * cosh(50 / x))) / x)


row = newton(f, df, 1, .01, 0.3651, 1, "Newton A Root 1")
row = newton(f, df, 2, .01, 1.92174, row, "Newton A Root 2")
row = newton(f, df, 3, .01, 3.56316, row, "Newton A Root 3")

newton(g, dg, 100, 0.01, 126.632, row, "Newton B Root")

book.close()
