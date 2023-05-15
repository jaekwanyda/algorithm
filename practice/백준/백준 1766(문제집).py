import heapq
#아이디어 : 위상정렬을 이용하면 해결할 수 있을 것 같다.
#연관되어 있는 것들은 그것들 중 가장 큰 수의 집합으로 묶고 그 안에서 위상정렬을 진행하면 될 것 같다.
#step 1: 아직 안나온 수 중 가장 작은 수를 뽑는다.
#step 2: 그 수 보다 만약 먼저 풀어야 될 문제가 있으면 앞에 둔다.
#n,m 입력 받기
n,m = map(int,input().split())
#간선 입력 받기
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split()) #a가 먼저 풀어야 할 문제, b는 그 뒤에 풀어도 되는 문제
    graph[a].append(b) #간선의 출발지점에 도착 지점 입력
    indegree[b]+=1
#들어오는 간선의 수가 0인 점들 모두 heapq에 넣기
q=[]
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)
#풀 수 있는 문제를 가장 작은 순서대로 뽑기
answer = []
while q:
    poss = heapq.heappop(q)
    answer.append(poss)
    #이어지는 간선이 있으면 간선을 없애고 indgree 줄이기
    for i in graph[poss]:
        indegree[i]-=1
        if indegree[i] == 0: #만약 이제 풀 수 있는 문제가 되었다면 heapq에 넣기
            heapq.heappush(q,i)

#출력
print(" ".join(map(str, answer)))