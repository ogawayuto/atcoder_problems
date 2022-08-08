import math

N, A, B = list(map(int, input().split()))
sum_n = (N * (N + 1)) / 2
if N >= A:
    d = int(math.floor(N / A))
    sum_a = ((A + A * d) * d) / 2
else:
    sum_a = 0
if N >= B:
    d = int(math.floor(N / B))
    sum_b = ((B + B * d) * d) / 2
else:
    sum_b = 0

C = int((A * B) / math.gcd(A, B))
if N >= C:
    d = int(math.floor(N / C))
    sum_c = ((C + C * d) * d) / 2
else:
    sum_c = 0

print(int(sum_n - sum_a - sum_b + sum_c))
