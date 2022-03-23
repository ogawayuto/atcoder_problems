N, T = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0

for i in range(N):
    if i == N - 1:
        ans += T
    else:
        ans += min(T, t[i + 1] - t[i])

print(ans)
