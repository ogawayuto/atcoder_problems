H, W = list(map(int, input().split()))
a = [list(input()) for _ in range(H)]

for i in range(H):
    if a[i] == ["."] * W:
        a[i] = ["n"] * W
for j in range(W):
    erase = True
    for i in range(H):
        if a[i][j] == "#":
            erase = False
            break
    if erase:
        for i in range(H):
            a[i][j] = "n"

for i in range(H):
    b = False
    for j in range(W):
        if a[i][j] != "n":
            print(a[i][j], end="")
            b = True
    if b:
        print("")
