
N, M =list(map(int,input().split()))
ab = [list(map(int,input().split())) for _ in range(N)]
cd = [list(map(int,input().split())) for _ in range(M)]


for i in range(N):
    record = [0]*M
    for j in range(M):
        record[j] = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
    print(record.index(min(record))+1)

