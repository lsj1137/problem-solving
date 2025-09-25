import math
n = int(input())
rest = list(map(int,input().split()))
leader, teammate = map(int,input().split())
answer = 0

for i in range(n):
    answer += 1
    rest[i] -= leader
    if rest[i]>0:
        answer += math.ceil(rest[i]/teammate)
print(answer)
