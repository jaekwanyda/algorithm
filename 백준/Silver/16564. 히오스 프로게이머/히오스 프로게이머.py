import sys
input = sys.stdin.readline
#아이디어: 이분탐색 
#n,k 입력 받기
n,k = map(int,input().split())
#k개의 캐릭터 레벨 정보 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
#start 는 0 end는 max(array) + k
start = 0
end = max(array) + k
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in array:
        total += max(mid - i,0)
    if total > k:
        end = mid - 1
    else:
        start = mid + 1
print(end)
