N = int(input())
a = list(map(int, input().split()))
free = 0
color = [False]*8

for i in range(N):
    if 0 <= a[i] and a[i] <= 399:
        color[0]=True
    elif 400 <= a[i] and a[i] <= 799:
        color[1]=True
    elif 800 <= a[i] and a[i] <= 1199:
        color[2]=True
    elif 1200 <= a[i] and a[i] <= 1599:
        color[3]=True
    elif 1600 <= a[i] and a[i] <= 1999:
        color[4]=True
    elif 2000 <= a[i] and a[i] <= 2399:
        color[5]=True
    elif 2400 <= a[i] and a[i] <= 2799:
        color[6]=True
    elif 2800 <= a[i] and a[i] <= 3199:
        color[7]=True
    else:
        free += 1

if color.count(True) == 0:
    m=1
    free-=1
else:
    m=color.count(True)
M=m+free
print(m,M)
    
