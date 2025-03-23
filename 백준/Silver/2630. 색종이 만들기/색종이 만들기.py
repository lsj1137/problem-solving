def check(pl):
  global rb, rw
  s = sum([sum(p) for p in pl])
  if s == len(pl)**2 or s==0:
    if s==0:
      rw += 1
    return True
  else:
    return False

def dp(p,d):
  result = 0
  if check(p):
    return 1
  l = len(p)
  newp = [[0]*(l//2) for _ in range(l//2)]
  for i in range(0,l//2):
    for j in range(0,l//2):
      newp[i][j] = p[i][j]
  result += dp(newp,d+1)
  for i in range(0,l//2):
    for j in range(l//2,l):
      newp[i][j-l//2] = p[i][j]
  result += dp(newp,d+1)
  for i in range(l//2,l):
    for j in range(0,l//2):
      newp[i-l//2][j] = p[i][j]
  result += dp(newp,d+1)
  for i in range(l//2,l):
    for j in range(l//2,l):
      newp[i-l//2][j-l//2] = p[i][j]
  result += dp(newp,d+1)
  return result

N = int(input())
rw, rb = 0,0
pp = [[0]*N for _ in range(N)]
for i in range(N):
  pp[i] = list(map(int,input().split()))
t = dp(pp,0)
rb = t-rw
print(rw)
print(rb)