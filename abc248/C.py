N, M, K = list(map(int, input().split()))
M -= 1
K -= N
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(0, min(K + 1, M + 1)):
    dp[1][i] = 1

for n in range(1, N):
    for x in range(K + 1):
        for s in range(min(M + 1, K - x + 1)):
            dp[n + 1][s + x] += dp[n][x]

ans = 0
for i in range(K + 1):
    ans += dp[N][i] % 998244353
    ans %= 998244353
print(ans)
