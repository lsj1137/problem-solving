def check(a,b,c):
  if a*a+b*b==c*c:
    return "right"
  else:
    return "wrong"

result = []
while (True):
  a,b,c = map(int, input().split())
  if (a==0 or b==0 or c==0):
    break
  abc = sorted([a,b,c])
  a=abc[0]
  b=abc[1]
  c=abc[2]
  result.append(check(a,b,c))
for re in result:
  print(re)