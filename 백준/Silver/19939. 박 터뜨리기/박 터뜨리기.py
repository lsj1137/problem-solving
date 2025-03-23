N,K = map(int,input().split())
st = K*(K+1)//2
if N>=st:
  if (N-st)%K==0:
    print(K-1)
  else:
    print(K)
else:
  print(-1)