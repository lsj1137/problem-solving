import sys
nlist = [1]*(101)
for _ in range(int(sys.stdin.readline())):
  N = int(sys.stdin.readline())
  if N>2:
    for i in range(3,N):
      nlist[i] = nlist[i-2]+nlist[i-3]
  print(nlist[N-1])
