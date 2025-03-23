import sys
n = int(sys.stdin.readline())
nl = list(map(int,sys.stdin.readline().split()))
best = nl[0]
bf = 0
for i in range(n):
  nxt = max(bf + nl[i],nl[i])
  if nxt>best:
    best = nxt
  bf = nxt
print(best)