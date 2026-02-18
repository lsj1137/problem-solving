N = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())))

done = [False]*M

time = 0
if boxes[M-1]>cranes[0]:
    time = -1
else:
    while False in done:
        index = M-1
        for c in cranes:
            while index>-1 and (done[index] or boxes[index]>c):
                index -= 1
            if index>-1:
                done[index] = True
        time += 1
print(time)