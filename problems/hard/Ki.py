import sys

N, Q = list(map(int, input().split()))
E = [[] for _ in range(N)]
ans = [0] * N
sys.setrecursionlimit(200000000)


def dfs(now, pa=-1):
    for x in E[now]:
        if x != pa:
            ans[x] += ans[now]
            dfs(x, now)


for i in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

for j in range(Q):
    p, x = list(map(int, input().split()))
    p -= 1
    ans[p] += x

dfs(0)

print(*ans)
