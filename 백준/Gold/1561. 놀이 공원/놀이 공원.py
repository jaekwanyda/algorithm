import sys
input = sys.stdin.readline
#아이디어: 최대 걸리는 시간에서 이분탐색으로 탄 학생 수를 구해보자
#n,m 입력 받기
n,m = map(int,input().split())
#m개의 놀이기구 시간 정보 입력 받기
array = list(map(int,input().split()))
#start 는 0 end 는 최대 시간(대충 어림잡아 제일 짧은 놀이기구 시간 * 학생 수)
start = 0
end = n * min(array)
#놀이기구 별 남은 시간 담는 list
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    t_list = [] #바로 탈 수 있는 놀이기구
    #놀이기구 별 mid 시간 까지 탄 학생수 더해주기
    for i in range(m):
        if mid%array[i] == 0:
            t_list.append(i)
            cnt += mid//array[i]
        else:
            cnt += mid//array[i]+1
    #만약 그 시간까지 탄 학생이 기존 학생수보다 많으면 end를 mid로
    if cnt+len(t_list) >= n:
        end = mid - 1
    else:
        start = mid + 1
cnt = 0
t_list = []
for i in range(m):
    if start%array[i] == 0:
        t_list.append(i)
        cnt += start//array[i]
    else:
        cnt += start//array[i]+1
while True:
    a = t_list.pop(0)
    cnt += 1
    if cnt == n:
        print(a+1)
        break