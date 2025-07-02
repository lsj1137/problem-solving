T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int,input().split())
    ingredient = []
    for _ in range(N):
        ingredient.append(list(map(int,input().split())))
    curState = (0, 0)
    que = [curState]
    nextQue = []
    for i in range(N):
        for state in que:
            nextQue.append((state[0], state[1]))
            if state[1]+ingredient[i][1]<=L:
                nextQue.append((state[0]+ingredient[i][0], state[1]+ingredient[i][1]))
        que = nextQue
        nextQue = []
    que.sort(key=lambda x:-x[0])
    answer = que[0][0]
    print(f'#{test_case} {answer}')