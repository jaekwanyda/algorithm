import heapq
#아이디어:가장 작은 수들을 꺼내 더한 뒤 최소 힙에 계속 넣어준다. 마지막 하나가 남을 때 까지 반복한다.
#N 입력받기
n = int(input())
#N-list 입력받기
n_list = []
#정렬하기
for _ in range(n):
    heapq.heappush(n_list,int(input()))
#결과 구하기
result = 0
while len(n_list)>1: #하나만 남으면 멈춘다
    a = heapq.heappop(n_list)
    b = heapq.heappop(n_list)
    result += (a+b)
    heapq.heappush(n_list,a+b)

print(result)
