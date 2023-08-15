import sys
input = sys.stdin.readline
#아이디어: 위상 변환을 양 방향으로 진행해주고 더했을 때 n-1이 되면 가능할 것 같다.
from collections import deque
#n,m 입력받기
n,m = map(int,input().split())
#키 정보 입력받기
t_list = [[] for _ in range(n+1)] #큰 학생 정보 담기
t_in = [0]*(n+1) # 큰 학생 진입차수
s_list = [[] for _ in range(n+1)] #작은 학생 정보 담기
s_in = [0]*(n+1) #작은 학생 진입차수
for _ in range(m):
    a,b = map(int,input().split()) #a학생이 b학생보다 작다
    t_list[a].append(b) 
    t_in[b] += 1 
    s_list[b].append(a) 
    s_in[a] += 1
t_q = deque()
answer_t = [set() for i in range(n+1)]
for i in range(1,n+1):
    answer_t[i].add(i)
for i,j in enumerate(t_in):
    if i!=0 and j==0: #진입차수가 0인 것 t_q에 넣어주기
        t_q.append(i)
while t_q:
    now = t_q.popleft()
    for t in t_list[now]:
        t_in[t] -= 1
        answer_t[t].update(answer_t[now]) #이동하는 곳에 이 전의 노드 정보들 update
        if t_in[t] == 0: #만약 새롭게 집입차수가 0이 되면 q에 넣어준다
            t_q.append(t)
s_q = deque()
answer_s = [set() for i in range(n+1)]
for i in range(1,n+1):
    answer_s[i].add(i)
for i,j in enumerate(s_in):
    if i!=0 and j==0: #진입차수가 0인 것 s_q에 넣어주기
        s_q.append(i)
while s_q:
    now = s_q.popleft()
    for s in s_list[now]:
        s_in[s] -= 1
        answer_s[s].update(answer_s[now]) #이동하는 곳에 이 전의 노드 정보들 updase
        if s_in[s] == 0: #만약 새롭게 집입차수가 0이 되면 q에 넣어준다
            s_q.append(s)
answer = 0
for i in range(1,n+1):
    answer_t[i].update(answer_s[i])
    if len(answer_t[i]) == n:
        answer += 1
print(answer)
