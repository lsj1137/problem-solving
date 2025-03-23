S = input()
z,o = 0,0
for i in range(len(S)):
  if i==0:
    if S[i] == '0':
      z += 1
    else:
      o += 1
  else:
    if S[i] == '1' and S[i-1] == '0':
      o += 1
    if S[i] == '0' and S[i-1] == '1':
      z += 1
print(min(o,z))