def toBi(n):
  r = ''
  while n>0:
    r += str(n%2)
    n//=2
  return r[::-1]

def toDec(n):
  r = 0
  for i in range(len(n)):
    r += int(n[i])*(2**(len(n)-i-1))
  return r

print(toBi(toDec(input())*17))