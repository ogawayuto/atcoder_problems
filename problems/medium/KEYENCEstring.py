S = list(input())
n = len(S)
ans = "NO"
key = list("keyence")

for i in range(n):
    for j in range(i, n + 1):
        inst = S.copy()
        del inst[i:j]
        if inst == key:
            ans = "YES"
            break


print(ans)
