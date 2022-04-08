sx, sy, tx, ty = list(map(int, input().split()))
dx = tx - sx
dy = ty - sy
ans = ""
ans += "R" * dx
ans += "U" * dy
ans += "L" * dx
ans += "D" * dy
ans += "D" + "R" * (dx + 1)
ans += "U" * (dy + 1) + "L"
ans += "U" + "L" * (dx + 1)
ans += "D" * (dy + 1) + "R"
print(ans)
