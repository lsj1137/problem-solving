import sys

N = sys.stdin.readline()
nums = list(map(int,sys.stdin.readline().split()))

numlist = sorted(list(set(nums)))
numlist = {numlist[i]:i for i in range(len(numlist))}
print(*[numlist[n] for n in nums])