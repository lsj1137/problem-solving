def solution(clothes):
    answer = 1
    types = {}
    for c in clothes:
        if c[1] in types:
            types[c[1]] += 1
        else:
            types[c[1]] = 1
    for k in types:
        answer *= types[k]+1
    answer -= 1
    return answer