from collections import defaultdict

S = list(input())
T = list(input())
d = defaultdict(lambda: "")
check = defaultdict(lambda: False)
ans = "Yes"
for i in range(len(S)):
    s = S[i]
    t = T[i]
    if d[s] == "":
        if check[t] == True:
            ans = "No"
            break
        d[s] = t
        check[t] = True
    elif d[s] == t:
        pass

U = []
for i in range(len(S)):
    s = S[i]
    t = T[i]
    if d[s] == "":
        pass
    else:
        s = d[s]
    if s != t:
        ans = "No"
        break

print(ans)
