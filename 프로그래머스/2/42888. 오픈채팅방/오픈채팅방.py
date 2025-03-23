def solution(record):
    answer = []
    name = {}
    for r in record:
        r = list(r.split())
        if r[0]!='Change':
            if r[0] == 'Enter':
                answer.append([r[1],'님이 들어왔습니다.'])
            else:
                answer.append([r[1],'님이 나갔습니다.'])
                continue
        name[r[1]] = r[2]
    answer = list(map(lambda x:name[x[0]]+x[1], answer))
    return answer