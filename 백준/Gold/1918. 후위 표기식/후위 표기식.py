priority = {
    '(':3, ')':3,
    '*':2, '/':2,
    '+':1, '-':1
}

S = input()
result = ''
op_stack = []

for c in S:
    if c not in priority:
        result += c
    elif c=='(':
        op_stack.append(c)
    elif c==')':
        while op_stack[-1]!='(':
            result += op_stack.pop()
        op_stack.pop()
    else:
        if len(op_stack)==0 or op_stack[-1] == '(' or priority[c]>priority[op_stack[-1]]:
            op_stack.append(c)
        else:
            while len(op_stack)>0 and priority[c]<=priority[op_stack[-1]] and op_stack[-1]!='(':
                result += op_stack.pop()
            op_stack.append(c)


while len(op_stack)>0:
    result += op_stack.pop()
print(result)