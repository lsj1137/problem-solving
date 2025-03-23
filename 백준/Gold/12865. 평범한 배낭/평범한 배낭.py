import sys

obj = [[0,0]]
N, K = map(int,sys.stdin.readline().split())
bag = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
  obj.append(list(map(int,sys.stdin.readline().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = obj[i][0] 
        v = obj[i][1]
        if j < w:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(v + bag[i - 1][j - w], bag[i - 1][j])

print(bag[N][K])