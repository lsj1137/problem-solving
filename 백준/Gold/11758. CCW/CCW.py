def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    result = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    if result > 0: return 1
    elif result < 0: return -1
    else: return 0

p1 = map(int, input().split())
p2 = map(int, input().split())
p3 = map(int, input().split())
print(ccw(p1,p2,p3))