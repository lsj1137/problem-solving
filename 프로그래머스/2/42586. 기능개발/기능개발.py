import math
def solution(progresses, speeds):
    answer = []
    for i in range(len(speeds)):
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])
    print(progresses)
    r = 1
    std = progresses[0]
    for i in range(len(speeds)-1):
        if std>=progresses[i+1]:
            r+=1
        else:
            answer.append(r)
            std = progresses[i+1]
            r = 1
    answer.append(r)
    return answer