
N,X = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range(N) ]
dp = [[False for i in range(X+1)] for j in range(N+1)] 
dp[0][0]=True
for i in range(N):
  a=ab[i][0]
  b=ab[i][1]
  for j in range(X):
    if dp[i][j] == True and  j+a < X+1 :
      dp[i+1][j+a] = True
    if dp[i][j] == True and  j+b < X+1 :
      dp[i+1][j+b] = True
if dp[N][X]:
  print('Yes')
  exit()
print('No')
