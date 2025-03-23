def bt(arr, l):
    if l==M:
        result.add(tuple(arr))
        return
    for i in range(N):
        l+=1
        arr.append(nl[i])
        bt(arr,l)
        arr.pop()
        l-=1
    return

N, M = map(int,input().split())
nl = sorted(list(map(int,input().split())))
result = set([])
l=0

bt([],l)
result = sorted(list(result))
for r in result:
    print(*r)