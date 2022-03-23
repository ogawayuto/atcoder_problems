S = list(input())
N = len(S)
for i in reversed(range(N)):
    if i % 2 == 1:
        continue
    else:
        if S[0 : int(i / 2)] == S[int(i / 2) : i]:
            print(i)
            exit()
