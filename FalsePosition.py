# John Berkley
# CS 301
# 7/8/2017

import xlsxwriter
from math import cosh, fabs

book = xlsxwriter.Workbook('falsepositive.xls')
sheet1 = book.add_worksheet()
sheet1.write(0, 0, "Procedure Name")
sheet1.write(0, 1, "Iteration")
sheet1.write(0, 2, "Current Value")
sheet1.write(0, 3, "Function Value")
sheet1.write(0, 4, "Relative Error")
sheet1.write(0, 5, "True Error")


def false_position(func, a, b, e, true_value, xls_initial_row, procedure_name):
    fa = func(a)
    fb = func(b)
    c = a + b / 2

    for n in range(100):
        prev_c = c
        c = b - ((fb * (b - a)) / (fb - fa))
        fc = func(c)
        rel_error = fabs((c - prev_c) / c)
        true_error = fabs(true_value - c) / true_value
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, c, fc))
        print('\tRelative Error: {} ; True Error: {}'.format(rel_error, true_error))
        if n == 0:
            sheet1.write(xls_initial_row + n, 0, procedure_name)
        sheet1.write(xls_initial_row + n, 1, n)
        sheet1.write(xls_initial_row + n, 2, c)
        sheet1.write(xls_initial_row + n, 3, fc)
        sheet1.write(xls_initial_row + n, 4, rel_error)
        sheet1.write(xls_initial_row + n, 5, true_error)
        if abs(rel_error) < e:
            print('\nConverged to Root\n')
            return xls_initial_row + n + 2
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


row = false_position(f, 0, 1, .01, 0.3651, 1, "False Position A Root 1")
row = false_position(f, 1, 2, .01, 1.92174, row, "False Position A Root 2")
row = false_position(f, 3, 4, .01, 3.56316, row, "False Position A Root 3")

false_position(g, 120, 130, .01, 126.632, row, "False Position B Root")

book.close()
