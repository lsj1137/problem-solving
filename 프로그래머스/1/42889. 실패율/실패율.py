def solution(N, stages):
    stages.sort()
    ls = len(stages)
    failratio = [[i+1,0] for i in range(N)]
    stage = 1
    fail = 0
    total = ls
    for i in range(ls):
        while stage<N and stages[i]!=stage:
            print(stage,fail,total)
            failratio[stage-1][1] = fail/total
            stage += 1
            total -= fail
            fail = 0
        if stages[i]==stage:
            fail += 1
    failratio[stage-1][1] = fail/total
    failratio.sort(key = lambda x:(-x[1],x[0]))
    answer = [x[0] for x in failratio]
    return answer