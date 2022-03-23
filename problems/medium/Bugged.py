N = int(input())
s = [int(input()) for _ in range(N)]
ans = sum(s)
s = [i for i in s if i % 10 != 0]
s.sort()

if ans % 10 != 0:
    ans
elif s:
    ans -= s[0]
else:
    ans = 0

print(ans)
