S = list(input())
id = [i for i, x in enumerate(S) if x == 'W']
count = 0
for i in range(len(id)):
  id[i] -= i 
  count += id[i]

print(count)
