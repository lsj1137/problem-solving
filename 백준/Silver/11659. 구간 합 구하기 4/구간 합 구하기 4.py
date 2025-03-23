import sys
N, M = map(int,sys.stdin.readline().split())
nl = list(map(int,sys.stdin.readline().split()))
sl = [0]*(N+1)
for i in range(1,N+1):
  sl[i] = sl[i-1]+nl[i-1]
for _ in range(M):
  s,f = map(int,sys.stdin.readline().split())
  print(sl[f]-sl[s-1])