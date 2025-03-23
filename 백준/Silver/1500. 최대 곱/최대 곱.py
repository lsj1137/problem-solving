import math
S, K = map(int,input().split())
if S%K==0:
  print((S//K)**K)
else:
  b,s = math.ceil(S/K), math.floor(S/K)
  for i in range(K):
    if b*i + s*(K-i) == S:
      break
  print(b**i*s**(K-i))