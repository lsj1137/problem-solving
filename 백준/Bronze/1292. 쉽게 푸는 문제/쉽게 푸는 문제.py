nl = []
for i in range(1,46):
  nl += [i]*i
s,f = map(int,input().split())
print(sum(nl[s-1:f]))