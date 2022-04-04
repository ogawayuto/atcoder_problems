N, M = list(map(int, input().split()))
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]
ans = False


def check(x, y):
    res = True
    for dy in range(M):
        if A[y + dy][x : x + M] != B[dy]:
            res = False
            break
    return res


for y in range(0, N - M + 1):
    for x in range(0, N - M + 1):
        if check(x, y):
            ans = True
            break
    if ans:
        break

if ans:
    print("Yes")
else:
    print("No")
