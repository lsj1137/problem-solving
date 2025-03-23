import sys; ip = sys.stdin.readline
from collections import deque

N, M = map(int,ip().split())
l,s = {},{}

for _ in range(N):
  nl = list(map(int,ip().split()))
  l[nl[0]] = nl[1]

for _ in range(M):
  ns = list(map(int,ip().split()))
  s[ns[0]] = ns[1]

t = 0
que = deque([1])
chk = [False]*101
nque = set([])
while 100 not in que:
  p = que.popleft()
  if not chk[p]:
    chk[p] = True
    for i in range(1,7):
      np = p+i
      if np in l:
        np = l[np]
      elif np in s:
        np = s[np]
      if np<101 and not chk[np]:
        nque.add(np)
  if not que:
    t += 1
    que = deque(nque)
    nque = set([])
print(t)