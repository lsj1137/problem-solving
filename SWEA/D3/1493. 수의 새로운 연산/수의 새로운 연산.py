def nToP(n):
    ny,cx,cy = 2,1,1
    i = 1
    while i<n:
        i += 1
        cx += 1
        cy -= 1
        if cy == 0:
            cy = ny
            cx = 1
            ny += 1
    return (cx,cy)

def pToN(x,y):
    ny,cx,cy = 2,1,1
    i = 1
    while cx!=x or cy!=y:
        i += 1
        cx += 1
        cy -= 1
        if cy == 0:
            cy = ny
            cx = 1
            ny += 1
    return i


T = int(input())
for test_case in range(1, T + 1):
    p,q = map(int, input().split())
    p1 = nToP(p)
    p2 = nToP(q)
    newP = (p1[0] + p2[0], p1[1] + p2[1])
    answer = pToN(newP[0], newP[1])
    print(f'#{test_case} {answer}')