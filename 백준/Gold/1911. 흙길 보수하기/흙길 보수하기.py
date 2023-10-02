import sys
input = sys.stdin.readline
#아이디어: heapq와 greedy를 이용하면 간단하게 해결될 것 같다.
import heapq
import math
#n,l 입력받기
n,l = map(int,input().split())
#웅덩이 정보 입력받기
pools = []
for _ in range(n):
    heapq.heappush(pools,list(map(int,input().split()))) #웅덩이 시작, 끝 정보 입력
#널빤지 위치 저장
board = 0
answer = 0
while pools:
    start,end = heapq.heappop(pools)
    start = max(board,start)
    #해당 웅덩이에 필요한 널빤지 개수 세주기
    answer += math.ceil((end-start)/l)
    board = start + math.ceil((end-start)/l)*l
print(answer) 