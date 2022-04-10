from collections import deque

H, W = list(map(int, input().split()))
N = int(input())
a = list(map(int, input().split()))
ans = [[0] * W for _ in range(H)]
q = deque()
for i in range(N):
    for j in range(a[i]):
        q.append(i + 1)
even = True

for i in range(H):
    if even:
        for j in range(W):
            ans[i][j] = q[0]
            q.popleft()
    else:
        for j in range(W - 1, -1, -1):
            ans[i][j] = q[0]
            q.popleft()
    even = not even

for i in range(H):
    print(*ans[i])
