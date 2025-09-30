# 소요시간 02:05:10
class Luggage:
    def __init__(self, i, h, w, x, y):
        self.index = i
        self.x, self.y = x, y
        self.h, self.w = h, w
    
    def __str__(self):
        return f'L{self.index}: [{self.x},{self.y}] h:{self.h},w:{self.w} |'

    def fall(self):
        while is_in(self.x+1, self.y) and not self.is_crashing(self.x+1, self.y):
            self.x += 1
        updateBoard(self)
        return

    def is_crashing(self, x, y):
        for i in range(x, x-self.h, -1):
            for j in range(y, y+self.w):
                if board[i][j] != 0:
                    return True
        return False

    def checkPop(self, isLeft):
        cx, cy = self.x, self.y
        if isLeft:
            while is_in(cx, cy):
                if self.is_crashing(cx, cy):
                    return False
                cy -= 1
        else:
            while is_in(cx, cy+self.w-1):
                if self.is_crashing(cx, cy):
                    return False
                cy += 1
        return True

def is_in(x, y):
    return -1<x<N and -1<y<N

def updateBoard(luggage):
    for i in range(luggage.x, luggage.x-luggage.h, -1):
        for j in range(luggage.y, luggage.y+luggage.w):
            board[i][j] = luggage.index
    return

def delBoard(luggage):
    for i in range(luggage.x, luggage.x-luggage.h, -1):
        for j in range(luggage.y, luggage.y+luggage.w):
            board[i][j] = 0
    return

def printBoard():
    for b in board:
        print(*b)
    return

def findPopable(isLeft):
    result = []
    for l in luggages:
        delBoard(l)
        if l.checkPop(isLeft):
            result.append(l)
        updateBoard(l)
    result.sort(key = lambda x: x.index)
    # print(*result)
    return result[0]

def removeLuggage(sl):
    global luggages
    newLuggages = []
    delBoard(sl)
    for l in luggages:
        if l.index!=sl.index:
            newLuggages.append(l)
    del sl
    luggages = newLuggages
    return

def work(isLeftWorker):
    selectedLuggage = findPopable(isLeftWorker)
    removeLuggage(selectedLuggage)
    answer.append(selectedLuggage.index)
    return

def rearrange():
    for l in luggages:
        delBoard(l)
        l.fall()
    return


N, M = map(int, input().split())
board = [[0]*N for _ in range(N)]
luggages = []
answer = []

for _ in range(M):
    line = list(map(int, input().split()))
    newLuggage = Luggage(line[0], line[1], line[2], line[1]-1, line[3]-1)
    newLuggage.fall()
    luggages.append(newLuggage)

while len(luggages)>0:
    work(True)
    rearrange()
    # printBoard()

    if len(luggages)==0:
        break

    work(False)
    rearrange()
    # printBoard()

for a in answer:
    print(a)
