def dfs(start, tickets):
    if len(tickets)==1:
        if start==tickets[0][0]:
            return [[start, tickets[0][1]]]
        else:
            return []
    result = []
    for i, t in enumerate(tickets):
        restTicket = tickets[:i]+tickets[i+1:]
        s, e = t[0], t[1]
        if s==start:
            temp = dfs(e, restTicket)
            for route in temp:
                result.append([start]+route)
    return result

def solution(tickets):
    answer = []
    routes = dfs("ICN", tickets)
    # print(routes)
    routes.sort()
    answer = routes[0]
    return answer