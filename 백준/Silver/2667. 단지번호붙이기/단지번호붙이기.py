import sys

def sametown(tl,y,x):
  result = set([])
  if tl[y][x]=='0':
    return result
  else:
    if not towncheck[y][x]:
      result.add((x,y))
      towncheck[y][x] = True
      if y>0:
        result.update(sametown(tl,y-1,x))
      if x>0:
        result.update(sametown(tl,y,x-1))
      if y<N-1:
        result.update(sametown(tl,y+1,x))
      if x<N-1:
        result.update(sametown(tl,y,x+1))
  return result

N = int(sys.stdin.readline())
townmap = []
towncheck = [[False]*N for _ in range(N)]
for _ in range(N):
  townmap.append(list(sys.stdin.readline().strip()))
town = []
for i in range(N):
  for j in range(N):
    r = sametown(townmap,i,j)
    if r:
      town.append(len(r))

print(len(town))
town.sort()
for t in town:
  print(t)