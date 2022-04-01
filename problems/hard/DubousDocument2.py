S = list(input())
T = list(input())
restorable = False
for i in range(len(S) - len(T), -1, -1):
    for j in range(len(T)):
        match = True
        if not (S[i + j] == T[j] or S[i + j] == "?"):
            match = False
            break
    if match:
        S = S[:i] + T + S[i + len(T) :]
        restorable = True
        break
if restorable:
    for i in range(len(S)):
        if S[i] == "?":
            S[i] = "a"
    print(*S, sep="")
else:
    print("UNRESTORABLE")
