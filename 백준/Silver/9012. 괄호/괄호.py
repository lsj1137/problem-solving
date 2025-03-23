import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
  zerosum = 0
  par = sys.stdin.readline().strip()
  for p in par:
    if p=='(':
      zerosum+=1
    else:
      zerosum-=1
    if zerosum<0:
      break
  if zerosum!=0:
    print("NO")
  else:
    print("YES")