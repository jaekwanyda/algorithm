import sys
input = sys.stdin.readline
#아이디어:heapq 사용
import heapq
#n,m입력받기
n,m = map(int,input().split())
q = list(map(int,input().split()))
heapq.heapify(q)
for _ in range(m):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q,a+b)
    heapq.heappush(q,a+b)
print(sum(q))
