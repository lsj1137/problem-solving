def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    filterIndex = 0
    sortIndex = 0
    if ext=='date':
        filterIndex = 1
    elif ext=='maximum':
        filterIndex = 2
    elif ext=='remain':
        filterIndex = 3
    if sort_by=='date':
        sortIndex = 1
    elif sort_by=='maximum':
        sortIndex = 2
    elif sort_by=='remain':
        sortIndex = 3
    data = list(filter(lambda x:x[filterIndex]<val_ext, data))
    answer = sorted(data, key=lambda a:a[sortIndex])
    return answer