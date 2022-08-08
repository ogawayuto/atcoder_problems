H, W = list(map(int, input().split()))
p = []
for i in range(H):
    t = list(input())
    if "o" in t:
        p.append([i, t.index("o")])
        t[t.index("o")] = "-"
    if "o" in t:
        p.append([i, t.index("o")])
print(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]))
