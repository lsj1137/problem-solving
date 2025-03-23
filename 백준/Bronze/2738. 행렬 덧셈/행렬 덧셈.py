import sys; ip = sys.stdin.readline

N,M = map(int,ip().split())
r = [[0]*M for _ in range(N)]
for _ in range(2):
    for i in range(N):
        l = list(map(int,ip().split()))
        for j in range(M):
            r[i][j] += l[j]
for rr in r:
    print(' '.join(map(str,rr)))