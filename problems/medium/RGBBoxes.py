R, G, B, N = list(map(int, input().split()))
ans = 0
cr = int(N / R) + 1

for r in range(cr):
    cg = int((N - r * R) / G) + 1
    for g in range(cg):
        rest = N - r * R - g * G
        if rest % B == 0 and rest / B >= 0:
            ans += 1

print(ans)
