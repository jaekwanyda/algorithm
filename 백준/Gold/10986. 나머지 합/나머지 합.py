import sys
from collections import Counter
input = sys.stdin.readline
#아이디어: 누적합 중 m으로 나눈 나머지들의 짝 개수가 m으로 나누어 떨어지는 것의 개수이다.
#N,M 입력받기
n,m = map(int,input().split())
#자연수 입력받기
array = list(map(int,input().split()))
array_sum = [0]
for i in array:
    array_sum.append((array_sum[-1]+i)%m)
sum_dic = dict(Counter(array_sum))
answer = 0
for key, item in sum_dic.items():
    answer += item*(item-1)//2
print(answer)