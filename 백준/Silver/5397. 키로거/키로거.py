import sys
input = sys.stdin.readline

class Node:
    def __init__(self, v):
        self.next = None
        self.prev = None
        self.value = v

class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def toString(self):
        res = []
        curNode = self.root.next
        while curNode is not None:
            res.append(curNode.value)
            curNode = curNode.next
        return ''.join(res)

    def add_node(self, cursor, node):
        cur_node = cursor
        child = cur_node.next
        if cur_node!=None:
            cur_node.next = node
            node.prev=cur_node
        if child!=None:
            node.next = child
            child.prev=node
        self.size += 1
        
    def remove_node(self, cursor):
        cur_node = cursor
        if cur_node==self.root:
            return
        parent = cur_node.prev
        child = cur_node.next
        if parent!=None:
            parent.next = child
        if child!=None:
            child.prev=parent
        self.size -= 1


for _ in range(int(input())):
    data = input().strip()
    result = LinkedList()
    result.root = Node('')
    cursor = result.root
    for c in data:
        if c=='<':
            cursor = cursor if cursor.prev==None else cursor.prev
        elif c=='>':
            cursor = cursor if cursor.next==None else cursor.next
        elif c=='-':
            result.remove_node(cursor)
            cursor = cursor if cursor.prev==None else cursor.prev
        else:
            result.add_node(cursor, Node(c))
            cursor = cursor if cursor.next==None else cursor.next
    print(result.toString())

