import sys

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):   #정방향 순회
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def insertBefore(self, next, newNode):  #노드 앞에 삽입
        newNode.prev = next.prev
        newNode.next = next
        next.prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def popBefore(self, next):   #앞에 노드 삭제
        result = next.prev
        self.nodeCount -= 1
        result.next.prev = result.prev
        result.prev.next = result.next
        return result.data

sdll = DoublyLinkedList()
s = list(sys.stdin.readline().strip())
now = sdll.tail
for c in s:
  sdll.insertBefore(now,Node(c))

for _ in range(int(sys.stdin.readline())):
  cmd = list(sys.stdin.readline().split())
  if cmd[0] == 'L':
    if now.prev and now.prev != sdll.head:
      now = now.prev
  if cmd[0] == 'D':
    if now.next :#and now.next != sdll.tail:
      now = now.next
  elif cmd[0] == 'B':
    if now.prev and now.prev != sdll.head:
      sdll.popBefore(now)
      
  elif cmd[0] == 'P':
    sdll.insertBefore(now, Node(cmd[1]))

print(''.join(sdll.traverse()))