import sys
import math
N,K = map(int,sys.stdin.readline().split())
st = [[0]*6 for _ in range(2)]
r = 0
for _ in range(N):
  S,Y = map(int,sys.stdin.readline().split())
  if S == 0:
    st[0][Y-1] += 1
  else:
    st[1][Y-1] += 1
for i in range(2):
  for j in range(6):
    r += math.ceil(st[i][j]/K)
print(r)