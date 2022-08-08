from itertools import combinations
from collections import defaultdict

N, K = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]
prev = set([])
ans = 0
d = defaultdict(int)
for i in range(1, N + 1):
    for t in combinations(list(range(N)), i):
        now = set(list(t))
        for j in now - prev:
            for alp in set(S[j]):
                d[alp] += S[j].count(alp)
        for j in prev - now:
            for alp in set(S[j]):
                d[alp] -= S[j].count(alp)
        tmp = list(d.values()).count(K)
        ans = max(ans, tmp)
        prev = now

print(ans)
