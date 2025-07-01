def check(n):
  strn = str(n)
  result = ''
  isThreeInside = False
  for c in strn:
    if c=='3' or c=='6' or c=='9':
      isThreeInside = True
      result += '-'
  if not isThreeInside:
    result = strn
  return result

N = int(input())
for i in range(1, N+1):
  print(check(i), end=' ')
