from collections import deque

N = int(input())
A = deque()
B = deque()
BA = deque()
ans = 0
s = [input() for _ in range(N)]
for i in range(N):
    if s[i][0] == "B" and s[i][-1] == "A":
        BA.append(s[i])
    elif s[i][0] == "B":
        B.append(s[i])
    elif s[i][-1] == "A":
        A.append(s[i])
    if "AB" in s[i]:
        ans += s[i].count("AB")

if BA:
    if A:
        A.pop()
        ans += 1
    if B:
        B.pop()
        ans += 1
    ans += len(BA) - 1

ans += min(len(A), len(B))
print(ans)
