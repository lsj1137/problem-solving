class Node:
    def __init__(self, value):
        self.value = value
        self.nextNodes = []

    def addNext(self, nextNode):
        self.nextNodes.append(nextNode)

T = 10
for test_case in range(1, T + 1):
    L, S = map(int, input().split())
    root = Node(S)
    nodesNum = list(map(int,input().split()))
    nodesDict = {S:root}
    checked = {S:False}
    for i in range(0,L,2):
        fromNode, toNode = Node(0), Node(0)
        if nodesNum[i] in nodesDict:
            fromNode = nodesDict[nodesNum[i]]
        else:
            fromNode = Node(nodesNum[i])
            nodesDict[nodesNum[i]] = fromNode
            checked[nodesNum[i]] = False
        if nodesNum[i+1] in nodesDict:
            toNode = nodesDict[nodesNum[i+1]]
        else:
            toNode = Node(nodesNum[i+1])
            nodesDict[nodesNum[i+1]] = toNode
            checked[nodesNum[i+1]] = False
        fromNode.addNext(toNode)
    que = [root]
    nextQue = []
    answer = 0
    while len(que)>0:
        curNode = que.pop()
        answer = max(answer, curNode.value)
        for node in curNode.nextNodes:
            if not checked[node.value]:
                checked[node.value] = True
                nextQue.append(node)
        if len(que) == 0:
            que = nextQue
            nextQue = []
            if len(que)!=0:
                answer = 0
    print(f'#{test_case} {answer}')