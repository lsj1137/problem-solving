N, M = map(int, input().split())
route = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf') for _ in range(3)] for _ in range(M)] for _ in range(N)]
dp[0] = [[x, x, x] for x in route[0]]

for i in range(1,N):
    for j in range(M):
        for k in range(3):
            dir = k-1
            if j+dir<0 or j+dir>M-1: continue
            candidates = []
            for l,cost in enumerate(dp[i-1][j+dir]):
                if l!=k:
                    candidates.append(cost)
            dp[i][j][k] = route[i][j]+min(candidates)

costs = []
for cost in dp[-1]:
    costs += cost
result = min(costs)
print(result)