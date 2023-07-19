import sys
input = sys.stdin.readline
#아이디어: 들어올때마다 회의실 확인하기=>O(N^2) 불가능
#greedy?
import heapq
#n입력받기
n = int(input())
q =[]
for _ in range(n):
    s,e = map(int,input().split())
    heapq.heappush(q,(s,e)) #시작 시간, 끝나는 시간
q_list=[];max_len=0
while q:
    s,e = heapq.heappop(q)
    while q_list:
        a = heapq.heappop(q_list)
        if a>s:
            heapq.heappush(q_list,a)
            break
    heapq.heappush(q_list,e)
    max_len = max(max_len,len(q_list))
print(max_len)
