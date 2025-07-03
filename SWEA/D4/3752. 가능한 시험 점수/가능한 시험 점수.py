T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    scores = list(map(int,input().split()))
    que = [0]
    nextQue = set([])
    index = 0
    while index<N:
        for score in que:
            nextQue.add(score+scores[index])
            nextQue.add(score)
        que = list(nextQue)
        nextQue = set([])
        index +=1
    result = len(que)
    print(f'#{test_case} {result}')