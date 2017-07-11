# John Berkley
# CS 301
# 7/8/2017


import xlsxwriter
from math import fabs, cosh

book = xlsxwriter.Workbook('bisection.xls')
sheet1 = book.add_worksheet()
sheet1.write(0, 0, "Procedure Name")
sheet1.write(0, 1, "Iteration")
sheet1.write(0, 2, "Current Value")
sheet1.write(0, 3, "Function Value")
sheet1.write(0, 4, "Relative Error")
sheet1.write(0, 5, "True Error")


def bisection(func, a, b, e, true_value, xls_initial_row, procedure_name):
    fa = func(a)
    fb = func(b)
    if not fa * fb < 0:
        print('{} : {}'.format(fa, fb))
        print('\nBracketing Condition Failed\n')
        return
    rel_error = b - a
    for n in range(100):
        rel_error /= 2
        c = a + rel_error
        fc = func(c)
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


row = bisection(f, 0, 1, .01, 0.3651, 1, "Bisection A Root 1")
row = bisection(f, 1, 2, .01, 1.92174, row, "Bisection A Root 2")
row = bisection(f, 3, 4, .01, 3.56316, row, "Bisection A Root 3")

bisection(g, 120, 130, .01, 126.632, row, "Bisection B Root")

book.close()
