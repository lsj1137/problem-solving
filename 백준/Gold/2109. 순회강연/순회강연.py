import sys
import heapq

T = int(sys.stdin.readline())
lectures = []
MAX_PAY = 0
for _ in range(T):
  pay, day = map(int,sys.stdin.readline().split())
  heapq.heappush(lectures,((-day,day),pay))
  if pay > MAX_PAY:
    MAX_PAY = pay

result = 0
pays = []
while MAX_PAY>0:
  while lectures and lectures[0][0][1]==MAX_PAY:
    high_pay = heapq.heappop(lectures)[1]
    heapq.heappush(pays, (-high_pay, high_pay))
    if not lectures:
      break
  if pays:
    result += heapq.heappop(pays)[1]
  MAX_PAY-=1
print(result)