import sys; ip = sys.stdin.readline
from collections import deque

N = int(ip())
tr = [[] for _ in range(N+1)]
rt = [[] for _ in range(N+1)]
chk = [False]*(N+1)
for _ in range(N-1):
  a,b = map(int,ip().split())
  tr[a].append(b)
  tr[b].append(a)
que = deque([1])
while que:
  r = que.popleft()
  if chk[r]:
    continue
  for n in tr[r]:
    if not chk[n]:
      rt[n] = r
  que+=tr[r]
  chk[r] = True
for rr in rt:
  if rr:
    print(rr)