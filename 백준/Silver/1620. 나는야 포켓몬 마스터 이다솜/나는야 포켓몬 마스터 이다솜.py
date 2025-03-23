import sys
n,m = map(int,sys.stdin.readline().split())
pdic = {}
for i in range(n):
  pdic[sys.stdin.readline().rstrip()] = i+1
pdic2 = {v:k for k,v in pdic.items()}
for _ in range(m):
  com = sys.stdin.readline().rstrip()
  if com in pdic:
    print(pdic[com])
  else:
    print(pdic2[int(com)])