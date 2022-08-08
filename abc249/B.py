S = input()
if S.islower():
    print("No")
    exit()
if S.isupper():
    print("No")
    exit()
S = list(S)
for i in range(len(S)):
    if S.count(S[i]) != 1:
        print("No")
        exit()
print("Yes")
