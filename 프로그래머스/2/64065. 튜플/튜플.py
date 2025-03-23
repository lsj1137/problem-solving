def solution(s):
    s = sorted(s.strip('{}').split('},{'),key = lambda x:len(x))
    answer = []
    for ns in s:
        ns = list(map(int,ns.split(',')))
        for n in ns:
            if n not in answer:
                answer.append(n)
    return answer