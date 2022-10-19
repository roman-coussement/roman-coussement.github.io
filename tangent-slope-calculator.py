from math import *


def f(x):
    return x ** 3


x = 3


def derive(x):
    h = 0.000000001
    slope = (f(x+h) - f(x)) / h
    return float("%.3f" % slope)


print(derive(x))
