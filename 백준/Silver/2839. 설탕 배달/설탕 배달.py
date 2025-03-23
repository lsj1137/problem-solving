n = int(input())
f = n//5
r = n%5
result = 0
if r==1:
  t=2
elif r==2:
  if n==7:
    result =-1
  else:
    t=4
elif r==3:
  t=1
elif r==4:
  if n==4:
    result=-1
  else:
    t=3
else:
  result=f
if result == 0:
  f=(n-3*t)//5
  result = t+f
print(result)