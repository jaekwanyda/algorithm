import sys
input = sys.stdin.readline
#아이디어: 그 순간 순간 가능한 작업을 바로 해주면 될 것 같다.
import heapq
#n 입력받기
n = int(input())
#작업들 정보 입력받기
works = [[] for _ in range(n+1)]
times = [0]*(n+1)
indegree = [0]*(n+1)
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    #시간 입력하기
    times[i] = tmp[0]
    #선행 개수 입력하기
    indegree[i] = tmp[1]
    #해당 작업이 완료 되었을 때 선행 작업 조건이 충족되는 것 입력하기
    for j in range(tmp[1]):
        works[tmp[2+j]].append(i)
q = []
for i in range(1,n+1):
    #선행 작업 없는 것 heapq에 넣기
    if indegree[i] == 0:
        heapq.heappush(q,(times[i],i)) #작업 완료 시간, 작업 번호
        indegree[i] = -1
while q:
    t,w = heapq.heappop(q)
    for i in works[w]: #선행 작업 처리해주기
        indegree[i] -= 1
    for i in range(1,n+1):
        #선행 작업 없는 것 heapq에 넣기
        if indegree[i] == 0:
            heapq.heappush(q,(times[i]+t,i)) #작업 완료 시간, 작업 번호
            indegree[i] = -1
    if not q:
        print(t)