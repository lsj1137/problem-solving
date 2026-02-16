import math
import sys

input = sys.stdin.readline

def c_round(n):
    if (n*10)%10>=5:
        return math.ceil(n)
    else:
        return math.floor(n)

n = int(input())
if n==0:
    print(0)
else:
    cut = c_round(n*0.15)
    scores = sorted([int(input()) for _ in range(n)])[cut:n-cut]
    print(c_round(sum(scores)/(n-cut-cut)))