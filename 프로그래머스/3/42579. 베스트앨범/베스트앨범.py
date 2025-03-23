def solution(genres, plays):
    answer = []
    lg = len(genres)
    dic = {}
    for i in range(lg):
        if genres[i] in dic:
            dic[genres[i]].append((plays[i],i))
            dic[genres[i]][0] += plays[i]
        else:
            dic[genres[i]] = [plays[i],(plays[i],i)]
    popular = sorted(dic.keys(),key = lambda x:-dic[x][0])
    print(dic)
    print(popular)
    for genre in popular:
        best2 = sorted(dic[genre][1:],key = lambda x:(-x[0],x[1]))
        answer.append(best2[0][1])
        if len(best2)>1:
            answer.append(best2[1][1])
    return answer