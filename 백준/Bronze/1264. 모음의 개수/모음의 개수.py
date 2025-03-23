import sys
ch = 'aeiou'
while True:
  r = 0
  l = sys.stdin.readline().strip()
  if l=='#':
    break
  for c in ch:
    for cc in l:
      if cc.lower() == c:
        r += 1
  print(r)