import bisect

Q = int(input())
C = []
r = []
X = []
B = []
s = 0
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        s += q[2]
        C.append([q[1], q[2]])
        X.append(q[1] * q[2])
        B.append(s)
    else:
        r.append(q[1])

ad = 0
last = -1
for i in range(len(r)):
    ans = 0
    rest = r[i] + ad
    index = bisect.bisect_right(B, rest) - 1
    if index >= 0:
        ad = B[index]
        rest -= B[index]
        ans += sum(X[last + 1 : index + 1])
    if rest > 0 and index + 1 < len(C) :
        ans += C[index + 1][0] * rest
        C[index + 1][1] -= rest
        X[index + 1] = C[index + 1][0] * C[index + 1][1]
        ad += rest
    last = index
    print(ans)
