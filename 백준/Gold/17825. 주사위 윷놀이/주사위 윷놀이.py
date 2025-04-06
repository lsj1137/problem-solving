class Node:
    value = 0
    child = None
    shortcut = None

    def __init__(self, value):
        self.value = value

    def setChild(self,childNode):
        self.child = childNode
        return self.child
    
    def setShort(self,shortNode):
        self.shortcut = shortNode
        return self.shortcut

    def next(self, isStart = False):
        if isStart and self.shortcut!=None:
            return self.shortcut
        else:
            return self.child
        
    def findNode(self, searchValue):
        if self.value==searchValue:
            return self
        else:
            if self.next()!=None:
                return self.next().findNode(searchValue)
            else:
                return None

def movePiece(startNode, move):
    finishNode = None
    for i in range(move):
        if i==0:
            finishNode = startNode.next(True)
        else:
            finishNode = finishNode.next()
        if finishNode.value==-1:
            break
    return finishNode

def copy(arr):
    newArr = []
    for content in arr:
        newArr.append(content)
    return newArr

points = [2,4,6,8,10, 12,14,16,18,20, 22,24,26,28,30, 32, 34, 36, 38, 40, -1]
pointsBranch1 = [13, 16, 19, 25, 30, 35]
pointsBranch2 = [22, 24]
pointsBranch3 = [28, 27, 26]
start = Node(0)
curNode = start
for p in points:
    nextNode = Node(p)
    curNode.setChild(nextNode)
    curNode = nextNode

shortStart1 = start.findNode(10)
shortStart2 = start.findNode(20)
shortStart3 = start.findNode(30)
curNode = shortStart1
branches = [pointsBranch1, pointsBranch2, pointsBranch3]
shortStarts = [shortStart1, shortStart2, shortStart3]
for i in range(3):
    curNode = shortStarts[i]
    for p in branches[i]:
        nextNode = Node(p)
        if p==branches[i][0]:
            curNode.setShort(nextNode)
        else :
            curNode.setChild(nextNode)
        curNode = nextNode
shortStart1.shortcut.findNode(35).setChild(start.findNode(40))
center = shortStart1.shortcut.findNode(25)
shortStart2.shortcut.findNode(24).setChild(center)
shortStart3.shortcut.findNode(26).setChild(center)

moves = list(map(int, input().split()))
scenarios = [[[start], 0]] # 경우의 수 저장용 리스트

for move in moves:
    newScenarios = []
    for scenario in scenarios:
        for startPosition in scenario[0]:
            nextPosition = movePiece(startPosition, move)
            newScenario = copy(scenario[0])
            if nextPosition.value==-1:
                newScenario.remove(startPosition)
                newScenarios.append([newScenario, scenario[1]])
                continue
            if nextPosition not in scenario[0]:
                newScenario.remove(startPosition)
                newScenario.append(nextPosition)
                newScenarios.append([newScenario, scenario[1]+nextPosition.value])
        if len(scenario[0])<10 and start not in scenario[0] and movePiece(start, move) not in scenario[0]:
            nextPosition = movePiece(start, move)
            newScenario = copy(scenario[0])
            newScenario.append(nextPosition)
            newScenarios.append([newScenario, scenario[1]+nextPosition.value])
    scenarios = newScenarios

answer = 0
for scenario in scenarios:
    answer = max(scenario[1], answer)
print(answer)