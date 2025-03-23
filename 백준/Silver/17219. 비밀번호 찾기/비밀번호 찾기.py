import sys

N,M = map(int, sys.stdin.readline().split())
site = {}
result = [0]*M
for _ in range(N):
  s, p = map(str,sys.stdin.readline().split())
  site[s] = p
for j in range(M):
  i = sys.stdin.readline().rstrip()
  result[j] = site[i]
print("\n".join(result))