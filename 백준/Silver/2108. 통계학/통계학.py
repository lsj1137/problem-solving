N = int(input())
num = []
ncount = {}
nsum = 0
for _ in range(N):
  n = int(input())
  num.append(n)
  if n in ncount:
    ncount[n]+=1
  else:
    ncount[n]=1

#최빈값
vl = list(ncount.values())
vl.sort(reverse = True)
freq = [k for k, v in ncount.items() if v == vl[0]]
freq.sort()
if len(freq)>1:
  freq = freq[1]
else:
  freq = freq[0]
#정렬
num.sort()
#평균
for n in num:
  nsum+=n

avg = round(nsum/N)


print(avg)
print(num[(len(num)-1)//2])
print(freq)
print(num[len(num)-1]-num[0])