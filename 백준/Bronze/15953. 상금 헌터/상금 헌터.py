import sys; ip = sys.stdin.readline
for _ in range(int(ip())):
    p = 0
    a,b = map(int,ip().split())
    if a!=0 and a<=21:
        if a==1:
            p += 500
        elif 1<a<=3:
            p += 300
        elif 3<a<=6:
            p += 200
        elif 6<a<=10:
            p += 50
        elif 10<a<=15:
            p += 30
        else:
            p += 10
    if b!=0 and b<=31:
        if b==1:
            p += 512
        elif 1<b<=3:
            p += 256
        elif 3<b<=7:
            p += 128
        elif 7<b<=15:
            p += 64
        else:
            p += 32
    print(p*10000)