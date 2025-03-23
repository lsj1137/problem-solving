a,b = map(str,input().split())
r = 0
for n1 in a:
  for n2 in b:
    r += int(n1)*int(n2)
print(r)