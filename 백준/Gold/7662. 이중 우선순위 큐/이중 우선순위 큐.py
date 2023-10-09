import sys
input = sys.stdin.readline
#아이디어: heapq를 2개 이용해보자
import heapq
#t 입력받기
t = int(input())
for _ in range(t):
    q = [] #최소힙
    p = [] #최대힙
    q_dict = {}
    p_dict = {}
    #연산개수 k 입력받기
    k = int(input())
    for _ in range(k):
        oper = input().rstrip()
        if oper[0] == 'I':
            heapq.heappush(q,int(oper[2:]))
            heapq.heappush(p,-int(oper[2:]))
        else:
            if q:
                if oper[2] == "1":
                    while p:
                        a = heapq.heappop(p)
                        if -a in p_dict and p_dict[-a]>0: #이미 지워진 내역이 있는 경우
                            p_dict[-a] -= 1
                        else: #실제로 지워진 경우
                            if -a in q_dict:
                                q_dict[-a] += 1
                            else:
                                q_dict[-a] = 1
                            break
                else:
                    while q:
                        a = heapq.heappop(q)
                        if a in q_dict and q_dict[a] > 0:
                            q_dict[a] -= 1
                        else:
                            if a in p_dict:
                                p_dict[a] += 1
                            else:
                                p_dict[a] = 1
                            break
    #연산이 끝난 후 q 확인
    while q:
        a = heapq.heappop(q)
        if a in q_dict and q_dict[a] > 0:
            q_dict[a] -= 1 
            continue
        else:
            heapq.heappush(q,a)
            break
    while p:
        a = heapq.heappop(p)
        if -a in p_dict and p_dict[-a] > 0:
            p_dict[-a] -= 1
            continue
        else:
            heapq.heappush(p,a)
            break
    if len(q) == 0:
        print('EMPTY')
    else:
        print(-heapq.heappop(p),heapq.heappop(q))
