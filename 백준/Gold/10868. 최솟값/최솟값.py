import sys; ip = sys.stdin.readline

def init(st,end,node):
    if st==end:
        segtree[node] = arr[st]
        return segtree[node]
    mid = (st+end)//2
    segtree[node] = min(init(st,mid,node*2),init(mid+1,end,node*2+1))
    return segtree[node]

def mini(st,end,node,left,right):
    if left>end or right<st:
        return float('inf')
    if left<=st and end<=right:
        return segtree[node]
    mid = (st+end)//2
    return min(mini(st,mid,node*2,left,right),mini(mid+1,end,node*2+1,left,right))

N,M = map(int,ip().split())
arr = []
for _ in range(N):
    arr.append(int(ip()))
segtree = [[] for _ in range(N*4)]
init(0,N-1,1)
for _ in range(M):
    a,b = map(int,ip().split())
    r = mini(0,N-1,1,a-1,b-1)
    print(r)