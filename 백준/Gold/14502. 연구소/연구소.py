import sys; ip = sys.stdin.readline
from itertools import combinations
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,M = map(int,ip().split())
lab = [list(map(int,ip().split())) for _ in range(N)]
blank,wall = [],[]
q = []

for i in range(N):
  for j in range(M):
    if lab[i][j] == 0:
      blank.append((i,j))
    elif lab[i][j] == 2:
      q.append((i,j))
    else:
      wall.append((i,j))

sq = q
block = list(combinations(blank,3))
safe = 0
for b in block:
  q = deque(sq[:])
  nq = []
  chk = [[False]*M for _ in range(N)]
  s = N*M-3
  for w in wall:
    chk[w[0]][w[1]] = True
    s -= 1
  for i in range(3):
    lab[b[i][0]][b[i][1]] = 1
    chk[b[i][0]][b[i][1]] = True
  while q:
    sp = q.popleft()
    x,y = sp[0],sp[1]
    if not chk[x][y]:
      s-=1
      chk[x][y] = True
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<N and -1<ny<M:
          if lab[nx][ny]!=1 and not chk[nx][ny]:
            nq.append((nx,ny))
    if not q:
      q = deque(nq)
      nq = []
  safe = max(safe,s)
  for i in range(3):
    lab[b[i][0]][b[i][1]] = 0
print(safe)