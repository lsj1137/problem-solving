import copy

def solution(friends, gifts):
    history = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    result = copy.deepcopy(history)
    fIndex = {}
    for i in range(len(friends)):
        fIndex[friends[i]] = i
    # print(fIndex)

    for g in gifts:
        a,b = g.split(' ')
        history[fIndex[a]][fIndex[b]] += 1
    print(history)
    
    for i in range(len(friends)):
        fIndex[friends[i]] = sum(history[i]) - sum(row[i] for row in history)
        
    print(fIndex)
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if history[i][j] > history[j][i]:
                result[i][j] += 1
            elif history[i][j] < history[j][i]:
                result[j][i] += 1
            elif fIndex[friends[i]]>fIndex[friends[j]]:
                result[i][j] += 1
            elif fIndex[friends[i]]<fIndex[friends[j]]:
                result[j][i] += 1
            
    # print(result)
    
    answer = max(sum(row) for row in result)
    return answer