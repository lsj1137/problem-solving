import math
w,h = map(int,input().split())
a = w+h
b = math.sqrt(w**2+h**2)
print(a-b)