T = int(input())
if T%10==0:
  A,B,C=0,0,0
  A += T//300
  T%=300
  B += T//60
  T%=60
  C += T//10
  print(A,B,C)
else:
  print(-1)