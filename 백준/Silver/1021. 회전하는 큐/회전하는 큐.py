def compare(l, st, fin, did):
  big = max(st,fin)
  sml = min(st,fin)
  gap1 = big - sml
  gap2 = l-gap1
  for d in did:
    if sml<d<big or sml == d:
      gap1-=1
    else:
      gap2-=1
  if gap1<gap2:
    return gap1
  else:
    return gap2

N,M = map(int, input().split())
nlist = [1]
nlist += list(map(int,input().split()))
done = []
r=0
for i in range(len(nlist)-1):
  r+=compare(N,nlist[i],nlist[i+1],done)
  done.append(nlist[i+1])
  
print(r)