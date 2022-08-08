from math import factorial


def f(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)
