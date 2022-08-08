from collections import defaultdict
import bisect

Q = int(input())
exist = []
d = defaultdict(int)
for i in range(Q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        x = t[1]
        d[x] += 1
        if d[x] == 1:
            bisect.insort(exist, x)
    if t[0] == 2:
        x = t[1]
        c = t[2]
        m = min(c, d[x])
        d[x] -= m
        if d[x] == 0 and m != 0:
            exist.pop(bisect.bisect_left(exist, x))
    if t[0] == 3:
        print(exist[-1] - exist[0])
