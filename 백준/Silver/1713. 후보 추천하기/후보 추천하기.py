import sys
input = sys.stdin.readline
#아이디어: 그냥 입력될때마다 sort 해주자
from collections import deque
#n 입력받기
n = int(input())
#추천학생 수 입력받기
k = int(input())
#추천 내역 입력받기
q = deque(map(int,input().split()))
n_list = []
cnt_list = []
while q:
    #현재 추천 받은 학생
    x = q.popleft()
    if x in n_list:
        cnt_list[n_list.index(x)] += 1
    elif len(n_list) < n:
        n_list.append(x)
        cnt_list.append(1)
    else:
        min_val = min(cnt_list)
        for i,val in enumerate(cnt_list):
            if val == min_val:
                n_list.pop(i)
                cnt_list.pop(i)
                break
        n_list.append(x)
        cnt_list.append(1)
print(*sorted(n_list))

