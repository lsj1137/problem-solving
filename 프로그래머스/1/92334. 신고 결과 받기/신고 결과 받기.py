def solution(id_list, report, k):
    ld = len(id_list)
    answer = [0] * ld
    dic = {}
    for i in range(ld):
        dic[id_list[i]] = i
    table = [[0] * ld for _ in range(ld+1)]
    for r in report:
        rspl = list(r.split())
        act = dic[rspl[0]]
        pas = dic[rspl[1]]
        if table[act][pas] == 0:
            table[act][pas] = 1
    for i in range(ld):
        total = sum([table[x][i] for x in range(ld)])
        table[ld][i] = total
    for i in range(ld):
        for j in range(ld):
            if table[i][j]==1 and table[ld][j]>=k:
                answer[i] += 1 
    return answer