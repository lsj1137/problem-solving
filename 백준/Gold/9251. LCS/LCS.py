import sys; ip = sys.stdin.readline

A = ip().strip()
B = ip().strip()

d = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
  for j in range(1,len(B)+1):
    if A[i-1] == B[j-1]:
      d[i][j] = d[i-1][j-1]+1
    else:
      d[i][j] = max(d[i][j-1],d[i-1][j])

print(d[-1][-1])