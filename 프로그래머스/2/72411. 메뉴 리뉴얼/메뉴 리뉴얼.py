from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        new = {}
        for o in orders:
            if len(o)>=c:
                can = list(combinations(o,c))
                for m in can:
                    nm = ''.join(sorted(m))
                    if nm in new:
                        new[nm] += 1
                    else:
                        new[nm] = 1
        if new:
            maxi = max(new.values())
            if maxi>1:
                for k in new:
                    if new[k] == maxi:
                        answer.append(k)
    answer.sort()
    return answer