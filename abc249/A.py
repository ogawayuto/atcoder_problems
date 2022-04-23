import math

A, B, C, D, E, F, X = list(map(int, input().split()))


def f(a, b, c, x):
    t = math.floor(x / (a + c))
    m = x % (a + c)
    res = b * t * a
    if m > a:
        res += a * b
    else:
        res += m * b
    return res


if f(A, B, C, X) > f(D, E, F, X):
    print("Takahashi")
elif f(A, B, C, X) < f(D, E, F, X):
    print("Aoki")
else:
    print("Draw")
