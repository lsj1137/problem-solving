import sys; ip = sys.stdin.readline
N = int(ip())
s = []
for _ in range(N):
  s.append(list(map(int,ip().split())))
s.sort()
t = 0
for x in s:
  if x[0]>t:
    t += x[0]-t
  t += x[1]
print(t)