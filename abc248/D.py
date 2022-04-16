N = int(input())
A = list(map(int, input().split()))
Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]
C = [[0] * (N + 1) for _ in range(N)]
C[0][A[0]] += 1
for i in range(1, N):
    C[i] = C[i - 1].copy()
    C[i][A[i]] = C[i - 1][A[i]] + 1

for l in q:
    L = l[0] - 1
    R = l[1] - 1
    X = l[2]
    if L == 0:
        print(C[R][X])
    else:
        print(C[R][X] - C[L - 1][X])
