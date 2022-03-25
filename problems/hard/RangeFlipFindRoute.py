H, W = list(map(int, input().split()))
s = [list(input()) for _ in range(H)]
deployed = {(0, 0)}
correct = set([])
score = [[200] * W for i in range(H)]
score[0][0] = 0

while True:
    loc = (-1, -1)
    min_score = 300
    for y, x in deployed:
        if score[y][x] < min_score:
            min_score = score[y][x]
            loc = (y, x)
    if loc == (H - 1, W - 1):
        break
    deployed.remove(loc)
    correct.add(loc)
    y = loc[0]
    x = loc[1]
    if y + 1 < H and (y + 1, x) not in correct:
        deployed.add((y + 1, x))
        if s[y + 1][x] == "#" and s[y][x] == ".":
            cost = 1
        else:
            cost = 0
        if score[y + 1][x] > score[y][x] + cost:
            score[y + 1][x] = score[y][x] + cost

    if x + 1 < W and (y, x + 1) not in correct:
        deployed.add((y, x + 1))
        if s[y][x + 1] == "#" and s[y][x] == ".":
            cost = 1
        else:
            cost = 0
        if score[y][x + 1] > score[y][x] + cost:
            score[y][x + 1] = score[y][x] + cost

if s[0][0] == "#":
    ans = score[H - 1][W - 1] + 1
else:
    ans = score[H - 1][W - 1]
print(ans)
