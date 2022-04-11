Q = int(input())
C = []
r = []


for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        C.append([q[1], q[2]])
    else:
        r.append(q[1])

for i in range(len(r)):
    sum = 0
    rest = r[i]
    while rest > 0:
        if C[0][1] > rest:
            C[0][1] -= rest
            sum += rest * C[0][0]
            rest = 0
        else:
            rest -= C[0][1]
            sum += C[0][0] * C[0][1]
            del C[0]
    print(sum)
