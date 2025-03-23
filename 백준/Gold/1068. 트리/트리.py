import sys
from collections import deque

def rmvq(tr,s,pr):
  q = deque([s])
  i = 0
  news = s
  while True:
    if news in tr.keys():
      for node in tr[news]:
        q.append(node)
    i+=1
    if i>len(q)-1:
      break
    news = q[i]
  return q

def dfs(tr,node):
  global count
  if node not in tr.keys() or len(tr[node])==0:
    count += 1
    return count
  for n in tr[node]:
    count = dfs(tr,n)
  return count

tree = {}
N = int(sys.stdin.readline())
done = list(range(N))
pl = list(map(int,sys.stdin.readline().split()))
count = 0

for i in range(N):
  p,c = pl[i],i 
  if p not in tree.keys():
    tree[p] = [c]
  else:
    tree[p].append(c)

r = int(sys.stdin.readline())
for n in tree.keys():
  if r in tree[n]:
    pr = n
rq = rmvq(tree,r,pr)
for n in rq:
  if n in tree.keys():
    del tree[n]

tree[pr].remove(r)

result = 0
if len(tree[-1])>0:
  root = tree[-1][0]
  result = dfs(tree,root)
print(result)