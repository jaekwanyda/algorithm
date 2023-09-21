import sys
input = sys.stdin.readline
#아이디어: heapq와 union,find를 이용해서 해결해보자
import heapq
#n,m,k 입력받기
n,m,k = map(int,input().split())
#발전소 번호 입력받기
stations = set(map(int,input().split()))
q = []
for _ in range(m):
    a,b,money = map(int,input().split())
    heapq.heappush(q,(money,a,b))
parent = [i for i in range(n+1)]
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
def union(a,b):
    parent_a = find(a)
    parent_b = find(b)
    #둘 다 이미 발전소랑 연결되어 있으면 생략
    if (parent_a in stations and parent_b in stations) or parent_a == parent_b:
        return False
    elif parent_a in stations:
        parent[parent_b] = parent_a
    elif parent_b in stations:
        parent[parent_a] = parent_b
    else: #아무것도 성립 안되면 그냥 작은걸 기준으로 union
        if parent_a < parent_b:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b
    return True
cnt = len(stations)
answer = 0
while q:
    money,a,b = heapq.heappop(q)
    if union(a,b):
        cnt += 1
        answer += money
    if cnt == n:
        break
print(answer)