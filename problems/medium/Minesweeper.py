H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
Dx = [0, 0, 1, 1, 1, -1, -1, -1]
Dy = [1, -1, 1, 0, -1, 1, 0, -1]


def search(x, y):
    count = 0
    for dx, dy in zip(Dx, Dy):
        if not (0 <= x + dx and x + dx < H):
            continue
        if not (0 <= y + dy and y + dy < W):
            continue
        if S[x + dx][y + dy] == "#":
            count += 1
    return count


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            S[i][j] = search(i, j)
for i in S:
    print(*i, sep="")
