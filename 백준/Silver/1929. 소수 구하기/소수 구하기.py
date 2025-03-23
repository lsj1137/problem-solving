import math

def pcheck(a):
  b = int(math.sqrt(a))
  check = [True]*(a+1)
  for i in range(2,b+1):
    if check[i]:
      for j in range(i+i,a+1,i):
        check[j]=False
  return [i for i in range(2,a+1) if check[i]]

M, N = map(int, input().split())

result1 = pcheck(M)
result2 = pcheck(N)

for r in range(len(result1)):
  if result1[r]==M:
    continue
  result2.remove(result1[r])
for re in result2:
  print(re)