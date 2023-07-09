import sys
input = sys.stdin.readline
#아이디어: 부분합 조합을 최적으로 찾는 방법을 생각해보자. 시간 복잡도가 O(N^2)면 실패이다.
from collections import Counter
import math
#부분합 행렬을 만들고 dictionary에 저장해 자신의 값과 k만큼 차이나는 것과 선택할 수 있는 경우의 수를 모두 더해주자
#n,k 입력받기
n,k = map(int,input().split())
#array 입력받기
array = list(map(int,input().split()))
#부분합 array 만들기
p_sum = [0]*(n+1) #1번째 원소도 선택해주려면 한개 더있어야 한다.
for i in range(n):
    p_sum[i+1] = p_sum[i]+array[i]
p_dict = dict(Counter(p_sum))
answer = 0
#k==0 일 때는 같은 수에서 2개를 뽑는 경우의 수를 모두 더해주면 된다.
if k==0:
    for i,j in p_dict.items():
        if j>=2:
            answer += math.comb(j,2)
else:
    #앞에서 부터 보면서 가면 된다.
    p_dict = {}
    for i in p_sum:
        if i-k in p_dict:
            answer += p_dict[i-k]
        if i in p_dict:
            p_dict[i] += 1
        else:
            p_dict[i] =1
print(answer)
