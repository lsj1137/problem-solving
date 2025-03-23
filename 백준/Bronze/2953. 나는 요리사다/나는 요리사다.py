sc = [sum(map(int,input().split())) for _ in range(5)]
win = max(sc)
print(sc.index(win)+1,win)