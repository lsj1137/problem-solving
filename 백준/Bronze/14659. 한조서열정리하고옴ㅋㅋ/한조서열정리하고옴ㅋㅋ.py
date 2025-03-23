import sys

N = int(sys.stdin.readline())
mts = list(map(int,sys.stdin.readline().split()))
result = [0]*N
for i in range(N):
  for j in range(i+1,N):
    if mts[j]<mts[i]:
      result[i]+=1
    else:
      break
print(max(result))