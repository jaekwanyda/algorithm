import sys
input = sys.stdin.readline
#아이디어: stack을 이용해서 현재 위치에서 보이는 빌딩 높이를 기록해보자
#N입력 받기
n = int(input())
#빌딩 높이들 입력받기
array = [0] + list(map(int, input().split()))
array_left = [0]*(n+1) #왼쪽에 몇개 볼 수 있는지
array_right = [0]*(n+1) #오른쪽에 몇개 볼 수 있는지
near_list =[1000000]*(n+1) #가까운 곳 index
#왼쪽부터 보이는 빌딩 확인해보기
left = []
for idx in range(1,n+1):
    h = array[idx]
    #자기 보다 왼쪽에 있는 빌딩 중 자기 보다 높이가 낮거나 같은 것들은 삭제
    while left:
        if array[left[-1]] <= h:
            left.pop()
        else:
            break
    #이제 idx 빌딩에서 보이는 빌딩만 남음
    array_left[idx] = len(left)
    #가까운 곳 기록해두기
    if left:
        if abs(idx - left[-1]) < abs(near_list[idx] - idx):
            near_list[idx] = left[-1]
    left.append(idx)
#마찬가지로 오른쪽부터 보이는 빌딩 확인해보기
right = []
for idx in range(n,0,-1):
    h = array[idx]
    #자기 보다 오른쪽에 있는 빌딩 중 자기 보다 높이가 낮거나 같은 것들은 삭제
    while right:
        if array[right[-1]] <= h:
            right.pop()
        else:
            break
    #이제 idx 빌딩에서 보이는 빌딩만 남음
    array_right[idx] = len(right)
    #가까운 곳 기록해두기
    if right:
        if abs(idx - right[-1]) < abs(near_list[idx] - idx):
            near_list[idx] = right[-1]
    right.append(idx)
#답안 출력하기
for idx in range(1,n+1):
    if array_left[idx] + array_right[idx]:
        print(array_left[idx] + array_right[idx], near_list[idx])
    else:
        print(0)