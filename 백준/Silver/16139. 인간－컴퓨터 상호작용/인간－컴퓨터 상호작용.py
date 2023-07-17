import sys
input = sys.stdin.readline
#아이디어: 부분합을 구현하면 될 것 같은데, 메모리 초과 걱정이 생긴다.
from collections import defaultdict
import copy
#문자열 입력받기
s = input()
s_list = list(s)
#각 alphabet 개수를 저장해주자
s_dict_list = [{} for _ in range(len(s)+1)]
for i,j in enumerate(s_list):
    s_dict_list[i+1] = s_dict_list[i].copy()
    if j in s_dict_list[i+1]:
        s_dict_list[i+1][j] += 1
    else:
        s_dict_list[i+1][j] = 1
#n 입력받기
n = int(input())
for _ in range(n):
    find_s, start, end = input().split()
    if find_s in s_dict_list[int(end)+1]:
        a = s_dict_list[int(end)+1][find_s]
    else:
        a=0
    if find_s in s_dict_list[int(start)]:
        b = s_dict_list[int(start)][find_s]
    else:
        b=0
    print(a-b)