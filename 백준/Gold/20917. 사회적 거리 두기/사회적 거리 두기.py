import sys
input = sys.stdin.readline
#아이디어: 이분탐색을 이용
#t입력받기
t = int(input())
#D값이 주어졌을 때 가능 여부를 판별해주는 함수
def possi(d,array,s):
    cnt = 1
    start = 0
    end = 0
    while end<len(array):
        if array[end] - array[start] >= d:
            cnt += 1
            start = end
        else:
            end += 1
    if cnt >= s:
        return True
    return False
for _ in range(t):
    #n,s 입력받기
    n,s = map(int,input().split())
    #콘센트 정보 입력받기
    array = list(map(int,input().split()))
    array.sort()
    #시작은 1 부터 끝은 array[-1]-array[0]
    start = 1
    end = array[-1] - array[0]
    while start <= end:
        mid = (start+end)//2
        if not possi(mid,array,s):
            end = mid -1
        else:   
            start = mid +1
    print(end)
