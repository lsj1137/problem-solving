import sys; ip = sys.stdin.readline

N,K = map(int,ip().split())
ps = [0]
ln = list(map(int,ip().split()))
for n in ln:
    ps.append(ps[-1]+n)
r = -float('inf')
for i in range(K,N+1):
    r = max(r,ps[i]-ps[i-K])
print(r)