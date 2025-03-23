x,y = map(int,input().split())
wr = 100*y//x
s,f = 0,x
if wr!=100 and wr!=99:
  oldwr = wr
  while f-s>1:
    c = (s+f)//2
    y += c
    x += c
    wr = int((y/x)*100)
    if wr>oldwr:
      f = c
    else:
      s = c
    y-=c
    x-=c
else:
  f = -1
print(f)
