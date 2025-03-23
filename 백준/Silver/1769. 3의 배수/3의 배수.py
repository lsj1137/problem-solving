N = list(input())

t = 0
while True:
  if len(N)==1:
    break
  r = 0
  t += 1
  for n in N:
    r += int(n)
  N = list(str(r))
print(t)
if int(N[0])%3==0:
  print("YES")
else:
  print("NO")