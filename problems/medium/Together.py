N = int(input())
a = list(map(int, input().split()))
M = max(a)+1
count=[0]*(M+2)

for i in range(N):
    count[a[i]]+=1
    if a[i]-1 == -1 :
        count[M+1]+=1
    else:
        count[a[i]-1]+=1
    count[a[i]+1]+=1

print(max(count))

