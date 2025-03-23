a,b = map(str, input().split())
l = max(len(a),len(b))
a = a.zfill(l+1)
b = b.zfill(l+1)
c = ['0']*(l+1)
for i in range(l,-1,-1):
  if a[i] != b[i]:
    if c[i] == '1':
      c[i-1] = '1'
      c[i] = '0'
      continue
    c[i] = '1'
  else:
    if a[i]=='1':
      if c[i] == '1':
        c[i-1] = '1'
        c[i] = '1'
        continue
      c[i] = '0'
      c[i-1] = '1'
    else:
      if c[i] == '1':
        continue
      c[i] = '0'
if int(''.join(c))!=0:
  j = -1
  while True:
    j += 1
    if j>l:
      break
    if c[j]!='0':
      break
  c = c[j:]
c = int(''.join(c))
print(c)
