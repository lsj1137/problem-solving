def solution(e, starts):
    answer = []
    ukukCountTable = [0]*(e+1)
    resultTable = [i for i in range(e+1)]
    for i in range(1,e+1):
        for j in range(i,e+1,i):
            ukukCountTable[j] += 1
    highest = ukukCountTable[e]
    for i in range(e,1,-1):
        if ukukCountTable[i-1] >= highest:
            highest = ukukCountTable[i-1]
        else:
            resultTable[i-1] = resultTable[i]
    for s in starts:
        result = resultTable[s]
        answer.append(result)
    return answer