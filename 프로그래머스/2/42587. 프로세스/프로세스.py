from collections import deque
def solution(priorities, location):
    answer = 0
    srt = sorted(priorities)
    fl = deque(range(len(priorities)))
    while fl:
        obj = fl.popleft()
        if priorities[obj] == srt[-1]:
            srt.pop()
            answer += 1
            if obj==location:
                break
        else:
            fl.append(obj)
    return answer