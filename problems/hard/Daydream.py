S = list(input())

index = 0
S.reverse()
ans = "YES"

while index < len(S):
    five = "".join(S[index : index + 5 :])
    six = "".join(S[index : index + 6 :])
    seven = "".join(S[index : index + 7 :])
    if five == "maerd":
        index += 5
    elif five == "esare":
        index += 5
    elif six == "resare":
        index += 6
    elif seven == "remaerd":
        index += 7
    else:
        ans = "NO"
        break
print(ans)
