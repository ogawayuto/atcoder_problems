a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
x = [0] * 300
y = [0] * 300
x[a[0] + 100] += 1
x[b[0] + 100] += 1
x[c[0] + 100] += 1

y[a[1] + 100] += 1
y[b[1] + 100] += 1
y[c[1] + 100] += 1

print(x.index(1) - 100, y.index(1) - 100)
