def tri(n, ll):
  l = ll[n-1]
  if n==1:
    tr = '*'
    return tr
  if n%2 == 0:
    tr = [[' ']*l for _ in range((l+1)//2)]
    for i in range(l):
      tr[0][i] = '*'
    for j in range(1,(l+1)//2):
      tr[j][j] = '*'
      tr[j][l-j-1] = '*'
  else:
    tr = [[' ']*l for _ in range((l+1)//2)]
    for j in range((l+1)//2):
      tr[j][l//2-j] = '*'
      tr[j][l//2+j] = '*'
    for i in range(l):
      tr[(l+1)//2-1][i] = '*'

  newtr = tri(n-1,ll)
  h = (ll[n-2]+1)//2
  if n%2 == 0:
    for i in range(1,h+1):
      for j in range(h+1,h+1+ll[n-2]):
        tr[i][j] = newtr[i-1][j-h-1]
  else:
    for i in range(h,h*2):
      for j in range(h+1,h+1+ll[n-2]):
        tr[i][j] = newtr[i-h][j-h-1]
  return tr

N = int(input())
LL = [1]+[5]*(N-1)
for i in range(2,N):
  LL[i] = (LL[i-1]+1)*2+1
tria = tri(N,LL)

h = (LL[N-1]+1)//2
if N%2==1:
  for i in range(h):
    for j in range(h+i,LL[N-1]):
      tria[i][j] = ''
else:
  for i in range(h):
    for j in range(i):
      tria[i][LL[N-1]-j-1] = ''
for t in tria:
  print("".join(t))