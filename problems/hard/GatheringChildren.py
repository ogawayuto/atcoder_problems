from itertools import groupby
import math


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def moved(r, le):
    res = [0] * (r[1] + le[1])
    rchild: int = math.floor(r[1] / 2) + (math.ceil(le[1] / 2))
    lchild: int = r[1] + le[1] - rchild
    res[r[1] - 1] = lchild
    res[r[1]] = rchild
    return res


S = input()
run = runLengthEncode(S)
S = list(S)
ans = []

for i in range(0, len(run), 2):
    ans.extend(moved(run[i], run[i + 1]))


print(*ans)
