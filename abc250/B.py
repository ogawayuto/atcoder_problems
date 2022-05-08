N, A, B = list(map(int, input().split()))
first_color = "W"
for i in range(N):
    S = []
    now = first_color
    for j in range(N):
        if now == "W":
            S += ["."] * B
            now = "B"
        else:
            S += ["#"] * B
            now = "W"
    for j in range(A):
        print(*S, sep="")
    if first_color == "W":
        first_color = "B"
    else:
        first_color = "W"
