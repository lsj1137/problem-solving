def solution(commands):
    answer = []
    # 값 저장 배열과 부모(대표) 저장 배열 초기화
    values = [['' for _ in range(51)] for _ in range(51)]
    parent = [[(r, c) for c in range(51)] for r in range(51)]

    # (r, c)의 대표를 찾는 함수 (경로 압축 적용)
    def find(r, c):
        if parent[r][c] == (r, c):
            return r, c
        pr, pc = parent[r][c]
        parent[r][c] = find(pr, pc)
        return parent[r][c]

    # 두 셀을 병합하는 함수
    def union(r1, c1, r2, c2):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)

        if (r1, c1) != (r2, c2):
            # (r1, c1) 셀의 값이 있을 경우 그 값을 유지
            if values[r1][c1]:
                parent[r2][c2] = (r1, c1)
            # (r1, c1) 셀의 값은 없고 (r2, c2)의 값만 있을 경우, 그 값을 유지
            else:
                parent[r1][c1] = (r2, c2)

    for command in commands:
        parts = command.split()
        cmd = parts[0]

        if cmd == 'UPDATE':
            if len(parts) == 4: # UPDATE r c value
                r, c, value = int(parts[1]), int(parts[2]), parts[3]
                pr, pc = find(r, c)
                values[pr][pc] = value
            else: # UPDATE value1 value2
                value1, value2 = parts[1], parts[2]
                for r in range(1, 51):
                    for c in range(1, 51):
                        pr, pc = find(r, c)
                        if values[pr][pc] == value1:
                            values[pr][pc] = value2

        elif cmd == 'MERGE':
            r1, c1, r2, c2 = map(int, parts[1:])
            if (r1, c1) != (r2, c2):
                union(r1, c1, r2, c2)

        elif cmd == 'UNMERGE':
            r, c = map(int, parts[1:])
            pr, pc = find(r, c)
            value_to_keep = values[pr][pc]

            # 병합 그룹에 속한 모든 셀을 찾아 분리
            cells_to_unmerge = []
            for i in range(1, 51):
                for j in range(1, 51):
                    if find(i, j) == (pr, pc):
                        cells_to_unmerge.append((i, j))
            
            for ur, uc in cells_to_unmerge:
                parent[ur][uc] = (ur, uc)
                values[ur][uc] = ''
            
            # 원래 (r, c) 셀에 값 부여
            values[r][c] = value_to_keep

        elif cmd == 'PRINT':
            r, c = map(int, parts[1:])
            pr, pc = find(r, c)
            if not values[pr][pc]:
                answer.append("EMPTY")
            else:
                answer.append(values[pr][pc])

    return answer