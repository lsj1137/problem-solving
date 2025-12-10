import sys
s = sys.stdin.readline().strip()
f = sys.stdin.readline().strip()
ind = len(f)
i,r = 0,0
while i<len(s):
  if s[i:i+ind] == f:
    i += ind
    r += 1
  else:
    i+=1
print(r)