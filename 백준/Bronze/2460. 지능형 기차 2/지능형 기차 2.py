r,c = 0,0
for _ in range(10):
    o,i = map(int,input().split())
    c -= o
    c += i
    r = max(r,c)
print(r)