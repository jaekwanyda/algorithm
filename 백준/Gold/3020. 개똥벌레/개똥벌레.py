import sys
input = sys.stdin.readline
#아이디어: 이진탐색으로 석순을 기준으로 잘랐을 때 잘라야하는 종유석 개수를 세주자
from bisect import bisect_right,bisect_left
n,h = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))
down = sorted(array[::2]) #석순
up = sorted(array[1::2]) #종유석
answer = float('inf')
answer_cnt = 1
k = n//2 #석순과 종유석 개수
for i in range(h):
    cut_down = k-bisect_right(down,i)
    cut_up = k-bisect_left(up,h-i)
    if cut_down+cut_up < answer:
        answer = cut_down+cut_up
        answer_cnt = 1
    elif cut_down+cut_up == answer:
        answer_cnt += 1
print(answer,answer_cnt)