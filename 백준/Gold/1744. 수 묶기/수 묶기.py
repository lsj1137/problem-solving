import sys
N = int(sys.stdin.readline())
nl = []
rl = []
for _ in range(N):
  nl.append(int(sys.stdin.readline()))
nl.sort()
minus, zero,plus,one = 0,0,0,0
pcheck = False
for i in range(N):
  if nl[i]<0:
    minus +=1
  if nl[i]==0:
    zero +=1
  if nl[i]==1:
    one += 1
  if nl[i]>1 :
    plus += 1

r = 0
if minus!=0:
  if minus%2==0:
    for i in range(0,minus,2):
      rl.append(nl[i]*nl[i+1])
  else:
    for i in range(0,minus-1,2):
      rl.append(nl[i]*nl[i+1])
    if zero==0:
      rl.append(nl[minus-1])
if one!=0:
  rl+=[1]*one
if plus!=0:
  nl = nl[-plus:]
  if plus%2==0:
    for i in range(plus-1,-1,-2):
      rl.append(nl[i]*nl[i-1])
  else:
    for i in range(plus-1,0,-2):
      rl.append(nl[i]*nl[i-1])
    rl.append(nl[0])
print(sum(rl))