import sys; ip = sys.stdin.readline
from bisect import bisect_left

N = int(ip())
A = list(map(int,ip().split()))
D = []

for i in range(N):
  ind = bisect_left(D,A[i])
  if ind<len(D):
    D[ind] = A[i]
  else:
    D.append(A[i])
print(len(D))