import math

N = int(input())
ans = 10

for i in range(1, math.ceil(math.sqrt(N)) + 1):
    if N % i == 0:
        ans = min(ans, len(str(math.floor(N / i))))

print(ans)
