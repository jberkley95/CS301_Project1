#John Berkley
#CS 301
#7/8/2017


from math import fabs, cosh


def newton(func, dfunc, x, e):#, true_value):
    fx = func(x)

    for n in range(100):
        fp = dfunc(x)
        d = fx / fp
        x -= d
        fx = func(x)
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, x, fx))
        #print('\tRelative Error: {} ; True Error: {}'.format(error, (abs(true_value - x) / true_value)))
        if fabs(d) < e:
            print('\nConverged To Root\n')
            return


def f(x):
    return (2 * (x ** 3)) - (11.7 * (x ** 2)) + (17.7 * x) - 5


def df(x):
    return (6 * (x ** 2)) - (23.4 * x) + 17.7


def g(x):
    return x + 10 - (x * cosh(50 / x))


def dg(x):
    return 1 - (((cosh(50 / x) * x) - (50 * cosh(50 / x))) / x)


newton(f, df, 1, 0.01)
newton(g, dg, 1, 0.01)
