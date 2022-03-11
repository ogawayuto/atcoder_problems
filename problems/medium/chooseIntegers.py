A, B, C = list(map(int, input().split()))

for i in range(100):
    if (A*i)%B == C:
        print("YES")
        exit()

print("NO")

