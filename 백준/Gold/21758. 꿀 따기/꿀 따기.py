import sys
input = sys.stdin.readline
#아이디어: 꿀통과 꿀벌은 각각 양 끝에 있는게 좋다(내 생각)=> (벌,통),(통,벌),(벌,벌) 순으로 탐색해보자
#n 입력받기
n = int(input())
#꿀 정보 입력받기
honey = list(map(int,input().split()))
#꿀통이 오른쪽 끝에 있을 경우
p_sum = [0]*(n+1)
for i in range(n):
    p_sum[i+1] = p_sum[i]+honey[i]
left = p_sum[-1]-p_sum[1]
answer = left
for i in range(1,n-1):
    answer = max(answer,left-honey[i]+(p_sum[-1]-p_sum[i+1]))
#꿀통이 왼쪽 끝에 있을 경우
honey.reverse()
p_sum = [0]*(n+1)
for i in range(n):
    p_sum[i+1] = p_sum[i]+honey[i]
right = p_sum[-1]-p_sum[1]
for i in range(1,n-1):
    answer = max(answer,right-honey[i]+(p_sum[-1]-p_sum[i+1]))
#꿀통이 사이에 있는 경우
for i in range(1,n-1):
    answer = max(answer,p_sum[i+1]-p_sum[1]+p_sum[-2]-p_sum[i])
print(answer)