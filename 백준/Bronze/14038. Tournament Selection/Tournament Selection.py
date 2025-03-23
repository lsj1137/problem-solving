r=0
for _ in range(6):
    if input()=="W":
        r+=1
if r==0:
    print(-1)
elif 0<r<3:
    print(3)
elif 2<r<5:
    print(2)
else:
    print(1)