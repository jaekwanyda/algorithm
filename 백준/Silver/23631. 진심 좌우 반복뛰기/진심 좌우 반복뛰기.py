import sys
input = sys.stdin.readline
#아이디어: 등차수열 합과 이분탐색을 이용하면 간단하게 해결될 것 같다
#t입력받기
t = int(input())
#등차가 k이고 x개 만큼 있을 때 합 구하는 함수
def sum_x(k,x):
    return k*(x+1)*x//2
for _ in range(t):
    #n,k 입력받기
    n,k = map(int,input().split())
    #시작은 0 부터 끝은 n//k 의 root개 
    start = 0
    end = int((n//k)**(1/2)*2) + 1
    while start <= end:
        mid = (start+end)//2
        if sum_x(k,mid) >= n-1:
            end = mid -1
        else:
            start = mid +1
    #위치, 방향 찾기
    direction = 1 #-1이면 Left , 1이면 Right
    if start % 2 == 0: #이번 방향이 홀수면 오른쪽, 짝수면 왼쪽
        direction = -1
    #이전의 위치에서 n-1이 될때까지 이동
    before = -1*direction*((end+1)//2)*k
    approach = before + (n-1-sum_x(k,end))*direction
    if n-1 == sum_x(k,start):
        direction *= -1
    if direction == 1:
        print(f"{approach} R")
    else:
        print(f"{approach} L")
    
