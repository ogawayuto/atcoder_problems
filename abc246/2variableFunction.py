def f(a, b):
    return a**3 + a * b**2 + a**2 * b + b**3


N = int(input())
j = 10**6
X = 10**20
for i in range(10**6):
    while j >= 0 and f(i, j) >= N:
        X = min(X, f(i, j))
        j -= 1
print(X)
