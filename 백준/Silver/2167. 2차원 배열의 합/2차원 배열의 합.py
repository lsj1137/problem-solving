import sys

N,M = map(int,sys.stdin.readline().split())
arr = [[0] for _ in range(N)]
for i in range(N):
  arr[i] = list(map(int,sys.stdin.readline().split()))
K = int(sys.stdin.readline())
s = 0
re = []
for _ in range(K):
  i,j,x,y = map(int,sys.stdin.readline().split())
  for k in range(i-1,x):
    for l in range(j-1,y):
      s += arr[k][l]
  re.append(s)
  s = 0

for r in re:
  print(r)