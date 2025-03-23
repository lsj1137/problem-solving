a,b,c = input().split()
A = int(a)
B = int(b)
C = int(c)

print("%d" %((A+B)%C))
print("%d" %(((A%C)+(B%C))%C))
print("%d" %((A*B)%C))
print("%d" %(((A%C)*(B%C))%C))