def solution(lottos, win_nums):
    mini,z = 0,0
    for n in lottos:
        if n!=0:
            if n in win_nums:
                mini += 1
        else:
            z += 1
    r = [mini+z,mini]
    for i in range(2):
        if r[i]<2:
            r[i] = 6
        else:
            r[i] = 7-r[i]
    answer = r
    return answer