import sys; ip = sys.stdin.readline
A = ip().strip()
B = ip().strip()
la,lb = len(A), len(B)
dp = [[0]*(la+1) for _ in range(lb+1)]
r = [0]*lb

for i in range(1,lb+1):
  for j in range(1,la+1):
    if B[i-1]==A[j-1]:
      dp[i][j] = dp[i-1][j-1]+1
  r[i-1] = max(dp[i])

print(max(r))