import sys; ip = sys.stdin.readline

N = int(ip())
table = [[float('inf')]*N for _ in range(N)]
M = int(ip())
for _ in range(M):
  a,b,w = map(int,ip().split())
  table[a-1][b-1] = min(table[a-1][b-1],w)

for i in range(N):    #거치는 점
  for j in range(N):    #행
    for k in range(N):  #렬
      if j==k:
        table[j][k] = 0
        continue
      table[j][k] = min(table[j][k],table[j][i]+table[i][k])

for t in table:
  for tt in t:
    print(0 if tt == float('inf') else tt ,end= ' ')
  print()