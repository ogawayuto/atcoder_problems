import bisect
import math
from math import factorial


def f(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)


n = int(input())
a = list(map(int, input().split()))
a.sort()
top = a[len(a) - 1]
t = math.floor(top / 2)
index = bisect.bisect_right(a, t)

if index == 0:
    ans = [top, a[-1:]]
if t - (top - a[index - 1]) >= top - a[index] - t:
    ans = [top, a[index - 1]]
else:
    ans = [top, a[index]]

print(*ans)
