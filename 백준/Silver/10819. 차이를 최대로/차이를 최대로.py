from itertools import permutations

N = int(input())
nl = list(map(int,input().split()))

arrs = list(permutations(nl,N))
r = 0
for arr in arrs:
    newr = 0
    for i in range(N-1):
        newr += abs(arr[i+1]-arr[i])
    r = max(r,newr)
print(r)