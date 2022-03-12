N = int(input())
txy = [list(map(int, input().split())) for _ in range(N)]
ans = 'Yes'
prev = [0,0,0]

for i in range(N):
  dis = abs(txy[i][1] - prev[1]) + abs(txy[i][2] - prev[2])
  time =  txy[i][0] - prev[0]
  if (time - dis )>= 0 and (time - dis)%2 == 0 :
    prev = txy[i]
  else :
    ans = 'No'
    break
print(ans)
    
