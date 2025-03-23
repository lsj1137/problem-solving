def solution(dartResult):
    answer = 0
    score = []
    i = 0
    while i<len(dartResult):
        if dartResult[i].isdigit():
            sc = int(dartResult[i])
            if dartResult[i+1] == '0':
                i+=1
                sc = 10
            if dartResult[i+1] == 'S':
                score.append(sc)
            elif dartResult[i+1] == 'D':
                score.append(sc**2)
            else:
                score.append(sc**3)
            if i<len(dartResult)-2 and dartResult[i+2] == '*':
                score[-1]*=2
                if len(score)>1:
                    score[-2]*=2
                i+=1
            elif i<len(dartResult)-2 and dartResult[i+2] == '#':
                score[-1]*=-1
                i+=1
            i += 1
        i += 1
    print(score)
    answer = sum(score)
    return answer