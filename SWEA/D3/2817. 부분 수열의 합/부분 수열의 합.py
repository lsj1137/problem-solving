T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int,input().split()))
    answer = 0
    que = [0]
    newQue = []
    index = 0
    while index<len(A):
        n = que.pop()
        newQue.append(n)
        if n+A[index]==K:
            answer += 1
        elif n+A[index]<K:
            newQue.append(n + A[index])
        if len(que)==0:
            que = newQue
            newQue = []
            index += 1
    print(f'#{test_case} {answer}')