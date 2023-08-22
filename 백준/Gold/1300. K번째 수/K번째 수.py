import sys
input = sys.stdin.readline
#아이디어: 이분탐색으로 그 수 보다 작은게 행렬에 몇개 존재하는지 찾아주자
#n 입력받기 
n = int(input())
#k 입력받기
k = int(input())
#시작수는 1, 끝 수는 n^2로 설정
start = 1
end = n**2
while start<=end:
    mid = (start+end) // 2
    cnt = 0
    #1부터 n까지 자기 보다 작은 수 찾기
    for i in range(1,n+1):
        cnt += min(n,mid//i)
    #만약 cnt가 k 보다 크다면 end를 mid로 바꿔주기
    if cnt >= k:
        end = mid - 1
    #반대의 경우는 start를 mid로
    else:
        start = mid + 1
    #만약 일치하면 정답
    answer = start
print(answer)