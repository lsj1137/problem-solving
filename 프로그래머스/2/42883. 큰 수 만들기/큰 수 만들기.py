def solution(number, k):
    answer = [];
    removed = [];
    for n in number:
        if len(answer) == 0:
            answer.append(n)
            continue
        if n>answer[-1] and len(removed)<k:
            while len(answer)>0 and n>answer[-1] and len(removed)<k:
                removed.append(answer.pop())
            answer.append(n)
        else :
            answer.append(n)
    answer = answer[:len(number)-k]
    answer = ''.join(answer)
    return answer