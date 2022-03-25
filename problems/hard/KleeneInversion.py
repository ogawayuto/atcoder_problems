N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = []
ans: int = 0
for i in range(N):
    countall = 0
    countafter = 0
    for j in range(N):
        if j < i and A[i] > A[j]:
            countall += 1
        elif j > i and A[i] > A[j]:
            countall += 1
            countafter += 1
    B.append([countall, countafter])

for i in range(N):
    if K % 2 == 1:
        ans += B[i][1] * K + B[i][0] * K * K - int(B[i][0] * K * int((K + 1) / 2))
    else:
        ans += B[i][1] * K + B[i][0] * K * K - int(B[i][0] * (K + 1) * int(K / 2))
ans = ans % (10**9 + 7)

print(ans)
