import sys; ip = sys.stdin.readline

N = int(ip())
A = list(map(int,ip().split()))
d = A[:]
for i in range(1,N):
  for j in range(i):
    if A[j]<A[i]:
      d[i] = max(d[i],d[j]+A[i])
print(max(d))