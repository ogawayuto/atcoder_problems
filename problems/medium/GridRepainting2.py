H, W = list(map(int, input().split()))
s = [list(input()) for _ in range(H)]
ans = "Yes"
black = []
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            black.append([i, j])


def paint(x, y):
    if (
        [x + 1, y] in black
        or [x - 1, y] in black
        or [x, y + 1] in black
        or [x, y - 1] in black
    ):
        return True
    else:
        False


for xy in black:
    if paint(*xy):
        continue
    else:
        ans = "No"
        break

print(ans)
