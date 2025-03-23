minx, miny = 10001, 10001
maxx, maxy = -10001, -10001
for _ in range(int(input())):
    x, y = map(int, input().split())
    minx = min(x, minx)
    miny = min(y, miny)
    maxx = max(x, maxx)
    maxy = max(y, maxy)
print((maxx-minx)*(maxy-miny))