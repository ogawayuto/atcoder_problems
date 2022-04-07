N, X, Y = list(map(int, input().split()))
X -= 1
Y -= 1
d = 0
ans = [0] * (N - 1)
for i in range(N):
    for j in range(i + 1, N):
        if i <= X and Y <= j:
            d = (j - i) - (Y - X) + 1
        elif i <= X and j <= X:
            d = j - i
        elif Y <= i and Y <= j:
            d = j - i
        elif X < i and Y <= j:
            d = min(j - i, i - X + j - Y + 1)
        elif i <= X and j < Y:
            d = min(j - i, X - i + Y - j + 1)
        elif X < i and j < Y:
            d = min(j - i, i - X + Y - j + 1)
        ans[d - 1] += 1
print(*ans, sep="\n")
