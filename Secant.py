# John Berkley
# CS 301
# 7/8/2017

import xlsxwriter
from math import cosh, fabs

book = xlsxwriter.Workbook('secant.xls')
sheet1 = book.add_worksheet()
sheet1.write(0, 0, "Procedure Name")
sheet1.write(0, 1, "Iteration")
sheet1.write(0, 2, "Current Value")
sheet1.write(0, 3, "Function Value")
sheet1.write(0, 4, "Relative Error")
sheet1.write(0, 5, "True Error")


def secant(func, x0, x1, e, true_value, xls_initial_row, procedure_name):
    for n in range(100):
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        rel_error = fabs((x2 - x1) / x2)
        true_error = fabs(true_value - x2) / true_value
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, x2, func(x2)))
        print('\tRelative Error: {} ; True Error: {}'.format(rel_error, true_error))
        if n == 0:
            sheet1.write(xls_initial_row + n, 0, procedure_name)
        sheet1.write(xls_initial_row + n, 1, n)
        sheet1.write(xls_initial_row + n, 2, x2)
        sheet1.write(xls_initial_row + n, 3, func(x2))
        sheet1.write(xls_initial_row + n, 4, rel_error)
        sheet1.write(xls_initial_row + n, 5, true_error)
        if fabs((x2 - x1) / x2) < e:
            print('\nConverged To Root\n')
            return xls_initial_row + n + 2
        else:
            x0 = x1
            x1 = x2


def f(x):
    return (2 * (x ** 3)) - (11.7 * (x ** 2)) + (17.7 * x) - 5


def g(x):
    return x + 10 - (x * cosh(50 / x))


row = secant(f, 0, 1, .01, 0.3651, 1, "Secant A Root 1")
row = secant(f, 1, 2, .01, 1.92174, row, "Secant A Root 2")
row = secant(f, 3, 4, .01, 3.56316, row, "Secant A Root 3")

secant(g, 120, 130, .01, 126.632, row, "Secant B Root")

book.close()
