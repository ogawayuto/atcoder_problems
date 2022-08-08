N = int(input())
A = list(map(int, input().split()))
A.sort()
sum = 0
key = -1
for i in range(N - 1):
    sum += A[i]
    if sum * 2 < A[i + 1]:
        key = i

print(N - (key + 1))
