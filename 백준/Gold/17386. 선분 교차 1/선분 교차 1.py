def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    result = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    if result > 0: return 1
    elif result < 0: return -1
    else: return 0

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A, B = (x1, y1), (x2, y2)
C, D = (x3, y3), (x4, y4)

# 판별
res1 = ccw(A, B, C) * ccw(A, B, D)
res2 = ccw(C, D, A) * ccw(C, D, B)

if res1 < 0 and res2 < 0:
    print(1)
else:
    print(0)