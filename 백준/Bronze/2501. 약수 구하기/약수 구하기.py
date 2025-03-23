A,B = map(int,input().split())
l = []
ll = 0
for i in range(1,A+1):
    if A%i==0:
        l.append(i)
        ll += 1
if B<=ll:
    print(l[B-1])
else:
    print(0)