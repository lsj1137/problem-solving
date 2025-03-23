def dcrz(nl):
  for i in range(len(nl)-1,-1,-1):
    if nl[i]==nl[i-1]:
      nl.pop(i)
      nl[i-1] *= 2
    if len(nl)==K:
      return True
  return False

N,K = map(int,input().split())
bottle = []
newn = N
while newn!=0:
  i=0
  while 2**i<newn+1:
    i+=1
  i-=1
  bottle.append(2**i)
  newn-=2**i
result = 0
if K<len(bottle):
  while not dcrz(bottle):
    result += bottle[-1]
    bottle.append(bottle[-1])

print(result)