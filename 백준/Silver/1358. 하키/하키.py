import math

def check(a,b):
    r = H//2
    if X<=a<=X+W and Y<=b<=Y+H:
        return True
    elif math.sqrt((X-a)**2+(Y+r-b)**2)<=r or math.sqrt((X+W-a)**2+(Y+r-b)**2)<=r:
        return True
    else:
        return False

W,H,X,Y,P = map(int,input().split())
r = 0
for _ in range(P):
    x,y = map(int,input().split())
    if check(x,y):
        r+=1
print(r)