import math
N, K, L = map(int,input().split())
m = 0
while K!=L:
  m += 1
  K = math.ceil(K/2)
  L = math.ceil(L/2)
print(m)