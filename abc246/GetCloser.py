import math

A, B = list(map(float, input().split()))
d = math.sqrt(A**2 + B**2)
print(A / d, B / d)
