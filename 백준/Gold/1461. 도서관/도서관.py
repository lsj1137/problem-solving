import sys

N, M = map(int,sys.stdin.readline().split())
books = list(map(int,sys.stdin.readline().split()))
minus = sorted([x for x in books if x<0])
plus = sorted([x for x in books if x>0],reverse = True)
if not minus:
  minus = [0]
if not plus:
  plus = [0]

end = max(abs(minus[0]),abs(plus[0]))
r = 0
for i in range(0,len(minus),M):
  r += abs(minus[i])*2
for i in range(0,len(plus),M):
  r += plus[i]*2
r -= end
print(r)