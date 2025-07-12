from collections import deque

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    l = deque(map(int,input().split()))
    while l[-1]>0:
        for i in range(1,6):
            n = l.popleft()
            if n-i>0:
                l.append(n-i)
            else:
                l.append(0)
                break
    answer = ' '.join(map(str,l))
    print(f'#{N} {answer}')