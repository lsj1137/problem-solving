import sys; ip = sys.stdin.readline

N = int(ip())
nl = [-1]*501
d = [1]*501
for _ in range(N):
  a,b = map(int,ip().split())
  nl[a] = b

for i in range(501):
  if nl[i]==-1:
    continue
  for j in range(i):
    if nl[j]==-1:
      continue
    if nl[j]<nl[i]:
      d[i] = max(d[i],d[j]+1)

print(N-max(d))