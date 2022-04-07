N = int(input())
A = list(map(int, input().split()))
m = 10**10
ans = 0
minus = 0
for i in range(N):
    m = min(m, abs(A[i]))
    if A[i] < 0:
        minus += 1
        ans -= A[i]
    else:
        ans += A[i]

if minus % 2 == 1:
    ans -= 2 * m

print(ans)
