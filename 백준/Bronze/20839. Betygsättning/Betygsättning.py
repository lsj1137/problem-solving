A,C,E = map(int,input().split())
a,c,e = map(int,input().split())
if A==a and C==c and E==e:
    print("A")
elif a>=A/2 and C==c and E==e:
    print("B")
elif C==c and E==e:
    print("C")
elif c>=C/2 and E==e:
    print("D")
else:
    print("E")