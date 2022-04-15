from cmath import inf


N, K = list(map(int, input().split()))
x = list(map(int, input().split()))
n = []
p = []
for i in range(N):
    if x[i] >= 0:
        p.append(x[i])
    else:
        n.append(-x[i])
p.sort()
n.sort()

ans = inf
for i in range(len(n)):
    if i in range(len(n)) and K - i - 2 in range(len(p)):
        ans = min(ans, n[i] * 2 + p[K - i - 2])
for i in range(len(p)):
    if i in range(len(p)) and K - i - 2 in range(len(n)):
        ans = min(ans, p[i] * 2 + n[K - i - 2])
if ans == inf:
    ans = 0
    if n == []:
        ans = p[K - 1]
    if p == []:
        ans = n[K - 1]
print(ans)
