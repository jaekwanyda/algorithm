import sys
input = sys.stdin.readline
#아이디어: 하이퍼 튜브를 통해서 가도록 bfs 등록
from collections import deque
#n,k,m 입력받기
n,k,m = map(int,input().split())
#이동 가능한 노드
graph = [[] for _ in range(n+m+1)]
visited_cnt = [0 for _ in range(n+m+1)]
q = deque()
for i in range(m):
    #서로 갈 수 있는 역들 입력받기
    possi_list = list(map(int,input().split()))
    #입력된 k개의 역들은 서로 갈 수 있다. 이때 나오는 경우의 수는 kC2
    for j in range(k):
        graph[possi_list[j]].append(n+i+1) #possi_list역들은 n+i번째 튜브와 연결
        graph[n+i+1].append(possi_list[j])
q.append(1)
visited_cnt[1] = 1
possi = False
while q:
    x = q.popleft()
    if x == n:
        print(visited_cnt[n])
        possi = True
        break
    for nx in graph[x]:
        if not visited_cnt[nx]:
            #만약 튜브로 연결된 거면 +1 안해도 됨
            if nx>n:
                visited_cnt[nx] = visited_cnt[x]
                q.append(nx)
            else:
                visited_cnt[nx] = visited_cnt[x] + 1
                q.append(nx)
if not possi:
    print(-1) 
