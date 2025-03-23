import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
for _ in range(int(input())):
    inputs = list(map(int,input().split(' ')))
    if inputs[0]==1:
        dq.appendleft(inputs[1])
    elif inputs[0]==2:
        dq.append(inputs[1])
    elif inputs[0]==3:
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif inputs[0]==4:
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    elif inputs[0]==5:
        print(len(dq))
    elif inputs[0]==6:
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif inputs[0]==7:
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])