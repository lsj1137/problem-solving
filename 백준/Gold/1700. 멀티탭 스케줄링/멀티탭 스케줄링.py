import sys
N,K = map(int,sys.stdin.readline().split())
pl = list(map(int,sys.stdin.readline().split()))
nextind = {}
for j in range(K):
  if pl[j] in nextind.keys():
    continue
  else:
    nextind[pl[j]] = 100
  for k in range(j+1,K):
    if pl[k]==pl[j]:
      nextind[pl[j]] = k
      break
use = pl[0:N]
r = 0
for i in range(K):
  use.sort(key = lambda x:nextind[x],reverse = True)
  for k in range(i+1,K):
    if pl[k]==pl[i]:
      nextind[pl[i]] = k
      break
    if k == K-1:
      nextind[pl[i]] = 100
  #print(pl[i],use,nextind[pl[i]])
  if pl[i] in use:
    continue
  use[0] = pl[i]
  if len(set(use))<N:
    continue
  r += 1
print(r)