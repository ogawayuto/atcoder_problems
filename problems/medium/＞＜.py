
S = list(input())
N=len(S) + 1
chl = [0]*N
chr = [0]*N
for i in range(N) :
  if i == 0:
    chl[i] = 0
  elif S[i-1] == '<':
    chl[i] = chl[i-1] + 1
  else :
    chl[i] = 0 

for i in reversed(range(N)):
  if i == N-1:
    chr[i] = 0
  elif S[i] == '>':
    chr[i] = chr[i+1] + 1
  else :
    chr[i] = 0 
ans = 0
for i in range(N):
  ans += max(chr[i],chl[i])
print(ans)



