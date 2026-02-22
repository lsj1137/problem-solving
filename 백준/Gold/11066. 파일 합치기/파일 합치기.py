import sys
input = sys.stdin.readline

def solve():
    K = int(input())
    pages = list(map(int, input().split()))
    
    # 누적 합 미리 구하기
    # sum_dist[i]는 0부터 i-1번째까지의 합
    sum_dist = [0] * (K + 1)
    for i in range(1, K + 1):
        sum_dist[i] = sum_dist[i-1] + pages[i-1]
    
    # DP 테이블 초기화
    # dp[i][j]: i번째부터 j번째까지 합치는 데 드는 최소 비용
    dp = [[0] * K for _ in range(K)]
    
    # 3. 구간 길이를 늘려가며 계산 (2개 합치기부터 K개 합치기까지)
    for length in range(1, K):
        for i in range(K - length):
            j = i + length # 끝점 j
            
            dp[i][j] = float('inf')
            # m은 i와 j 사이를 가르는 지점
            for m in range(i, j):
                # 점화식: (왼쪽 비용 + 오른쪽 비용) + 현재 구간의 파일 총합
                cost = dp[i][m] + dp[m+1][j] + (sum_dist[j+1] - sum_dist[i])
                if dp[i][j] > cost:
                    dp[i][j] = cost
                    
    print(dp[0][K-1])

T = int(input())
for _ in range(T):
    solve()