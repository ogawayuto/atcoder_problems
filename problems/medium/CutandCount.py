N = int(input())
S = list(input())
ans = 0

for i in range(N):
    count = []
    first_half = S[:i]
    second_half = S[i:]
    for j in first_half:
        e = j
        if (e not in count) and e in second_half:
            count.append(e)
    ans = max(ans, len(count))

print(ans)
