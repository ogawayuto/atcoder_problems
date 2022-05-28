a, b, c = list(map(int, input().split()))
if a <= b and b <= c:
    print("Yes")
    exit()
if b <= a and c <= b:
    print("Yes")
    exit()
print("No")
