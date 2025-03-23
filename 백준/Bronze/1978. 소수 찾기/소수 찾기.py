n = int(input())
nlist = list(map(int,input().split()))
count=0
for i in nlist:
  rest=0
  for j in range(1, i+1):
    if i%j==0:
      rest+=1
    if j==i:
      if rest==2:
        count+=1   
    
print(count)