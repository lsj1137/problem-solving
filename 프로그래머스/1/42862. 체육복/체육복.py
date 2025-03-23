def solution(n, lost, reserve):
    answer = 0
    chk = [False]*(n+1)
    for x in reserve:
        if x in lost:
            lost.remove(x)
            continue
        chk[x] = True
    lost.sort()
    for x in lost:
        if x>1 and chk[x-1]:
            chk[x-1] = False
            continue
        if x<n and chk[x+1]:
            chk[x+1] = False
            continue
        n -= 1
    print(chk)
    answer = n
    return answer