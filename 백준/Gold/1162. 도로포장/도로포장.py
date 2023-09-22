import sys
input = sys.stdin.readline
#아이디어: dp를 이용해서 전의 0~k번 생략했을 떄의 정보를 받아 최솟값을 갱신해주자
import heapq
# n, m, k 입력받기
n, m, k = map(int, input().split())
# 간선 정보 입력받기
graph = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, money = map(int, input().split())
    if (b in graph[a] and money < graph[a][b]) or b not in graph[a]:
        graph[a][b] = money
        graph[b][a] = money
q = []
heapq.heappush(q,(0,1,0)) #비용, 위치, 생략한 횟수 입력
# DP 배열 초기화
# dp[i][j]: i번 노드까지 사용해서 j번 생략한 경우의 최소 비용
dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
dp[1][0] = 0# 시작 노드는 생략하지 않음
while q:
    money, node, cnt = heapq.heappop(q)
    if money > dp[node][cnt]: #이미 최선인 노드는 생략
        continue
    if node == n:
        print(money)
        break
    for neighbor, cost in graph[node].items():
        # node에서 neighbor로 이동하는게 더 좋은 경로인 경우
        if dp[neighbor][cnt] > cost + money:
            dp[neighbor][cnt] = cost + money
            heapq.heappush(q,(cost + money,neighbor,cnt))
        # node에서 neighbor로 생략하고 이동하는게 더 좋은 경로인 경우
        if cnt<k and dp[neighbor][cnt+1] > money:
            dp[neighbor][cnt + 1] = money
            heapq.heappush(q,(money,neighbor,cnt+1))
