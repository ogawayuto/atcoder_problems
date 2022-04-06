N = int(input())
S = list(input())
ans = set([])

for i in range(1000):
    num = list(str(i).rjust(3, "0"))
    itr = 0
    for j in range(N):
        if num[itr] == S[j]:
            itr += 1
        if itr == 3:
            break
    if itr == 3:
        ans.add(i)

print(len(ans))
