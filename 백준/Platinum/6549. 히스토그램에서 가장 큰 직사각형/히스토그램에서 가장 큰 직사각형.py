import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = arr[0]
    h_arr = arr[1:] + [0] 
    stack = []
    result = 0
    for i in range(n + 1):
        # 현재 높이가 스택 top의 높이보다 낮으면 pop 시작
        while stack and h_arr[stack[-1]] >= h_arr[i]:
            top_idx = stack.pop()
            h = h_arr[top_idx]
            # 스택이 비었다면 0번부터 i-1번까지 전부 h 이상의 높이라는 뜻
            width = i if not stack else i - stack[-1] - 1
            result = max(result, h * width)
        stack.append(i)
    print(result)