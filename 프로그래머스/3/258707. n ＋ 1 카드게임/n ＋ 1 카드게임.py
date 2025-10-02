def solution(coin, cards):
    answer = 1
    N = len(cards)
    checked = [[False,0] for _ in range(N+1)]
    pairArr = []
    for i in range(N//3):
        nthCard = cards[i]
        pairCard = N+1-nthCard
        checked[nthCard][0] = True
        if checked[pairCard][0]:
            pairArr.append([0, 0])
    # print(pairArr)

    for i in range(N//3, N, 2):
        curRound = (i-N//3)//2+1
        if answer<curRound:
            break
        for j in range(2):
            nthCard = cards[i+j]
            pairCard = N+1-nthCard
            checked[nthCard][0] = True
            checked[nthCard][1] = 1
            if checked[pairCard][0]:
                pairArr.append([curRound, checked[nthCard][1]+checked[pairCard][1]])
        # print(i, pairArr)
        if len(pairArr)<1:
            continue
        pairArr.sort(key=lambda x:-x[1])
        pair = pairArr.pop()
        if coin < pair[1]:
            break
        else:
            coin -= pair[1]
            answer += 1
            
    return answer