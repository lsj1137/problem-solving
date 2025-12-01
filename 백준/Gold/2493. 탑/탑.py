N = int(input())
towers = list(map(int, input().split()))
result = []

stack = [(0,0)]
for (i, height) in enumerate(towers):
    j = len(stack)-1
    while stack[j][1]<height and j>0 and len(stack)>0:
        stack.pop()
        j -= 1
    if len(stack)==1:
        result.append(0)
    else:
        result.append(stack[-1][0]+1)
    stack.append((i, height))

print(*result)