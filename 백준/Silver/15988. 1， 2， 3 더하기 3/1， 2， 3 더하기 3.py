import sys
input = sys.stdin.readline

T = int(input().strip())
nl = [int(input().strip()) for _ in range(T)]

arr = [0]*1000001
arr[1] = 1
arr[2] = 1
arr[3] = 1
for i in range(1000001):
    for j in [1,2,3]:
        if i-j>-1:
            arr[i] = (arr[i] + arr[i-j]) % 1000000009

for n in nl:
    print(arr[n])