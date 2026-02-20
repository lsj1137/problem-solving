N = int(input())
left = list(map(int, input().split()))

height = [0]*N

for i,l in enumerate(left):
    index = 0
    while height[index]!=0:
        index += 1
    while l>0:
        index += 1
        if height[index]==0:
            l -= 1
    height[index] = i+1
print(*height)