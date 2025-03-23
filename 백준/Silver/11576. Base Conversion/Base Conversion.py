A,B = map(int,input().split())
m = int(input())
N = list(map(int,input().split()))
d = 0
for i in range(len(N)):
  d += N[i]*A**(len(N)-i-1)
r = []
while d>0:
  r.append(str(d%B))
  d//=B
r = r[::-1]
print(' '.join(r))