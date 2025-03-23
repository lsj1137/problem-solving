import heapq
descNum = [0,1,2,3,4,5,6,7,8,9]
ns = ['0','1','2','3','4','5','6','7','8','9']
N = int(input())
for dn in descNum:
    for n in ns:
        if n>str(dn)[0]:
            descNum.append(int(n+str(dn)))
descNum.sort()
if N>=len(descNum):
    print(-1)
else:
    print(descNum[N])