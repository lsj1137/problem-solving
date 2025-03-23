import math
S = input()
s = math.ceil(len(S)/2)
c,r = 0,len(S)*2
for i in range(s,len(S)):
  std = S[i:]
  if std[::-1]==S[i-len(std):i]:
    r = min(r, len(S)*2-len(std)*2)
  if std[::-1]==S[i-len(std)-1:i-1]:
    r = min(r, len(S)*2-len(std)*2-1)
r = min(r,len(S)*2-1)
print(r)