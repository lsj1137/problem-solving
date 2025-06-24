import math

def solution(s):
    answer = 1000
    for i in range(1,math.floor(len(s)/2)+1):
        repeat = 1
        tempAns = 0
        for j in range(0, len(s), i):
            # print(s[j:j+i], s[j+i:j+2*i], repeat, tempAns);
            if s[j:j+i] == s[j+i:j+2*i]:
                repeat += 1
            else:
                if repeat>1:
                    tempAns += i+len(str(repeat))
                    repeat = 1
                else :
                    tempAns += len(s[j:j+i])
        answer = min(answer, tempAns)
    if len(s)==1:
        answer = 1
    return answer