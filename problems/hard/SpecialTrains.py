import math

N = int(input())
C = [0] * N
S = [0] * N
F = [0] * N
ans = []
for i in range(1, N):
    C[i], S[i], F[i] = list(map(int, input().split()))

for i in range(1, N + 1):
    st = i
    now = 0
    while st < N:
        if now < S[st]:
            now = S[st] + C[st]
            st += 1
        else:
            now = math.ceil((now - S[st]) / F[st]) * F[st] + S[st] + C[st]
            st += 1
    ans.append(now)

print(*ans, sep="\n")
