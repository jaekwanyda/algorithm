import sys
input = sys.stdin.readline
#아이디어: 계속해서 4등분해 나가는 재귀함수를 구현하면 해결될 것 같다.
#n,r,c 입력받기
n,r,c = map(int,input().split())
def z(n,r,c):
    if n == 0:
        return 0
    order = 0 #z순서대로 0,1,2,3 사분면으로 구분하자
    if r >= 2**(n-1):
        order += 2 
        r -= 2**(n-1) #다음 재귀로 가기전 사각형 위치 왼쪽 위로 맞춰주자
    if c >= 2**(n-1):
        order += 1
        c -= 2**(n-1) #마찬가지
    return 2**(2*n-2)*order + z(n-1,r,c)
print(z(n,r,c))