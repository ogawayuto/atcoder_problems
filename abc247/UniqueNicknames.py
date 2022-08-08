N = int(input())
s = [0] * N
t = [0] * N
al = []
ans = "Yes"
for i in range(N):
    s[i], t[i] = input().split()

for i in range(N):
    a = s.copy()
    b = t.copy()
    n1 = a[i]
    del a[i]
    n2 = b[i]
    del b[i]
    if n1 not in a and n1 not in b:
        continue

    if n2 not in a and n2 not in b:
        continue
    else:
        ans = "No"

print(ans)
