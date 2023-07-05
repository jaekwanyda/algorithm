import sys
input = sys.stdin.readline
#아이디어:단순히 유클리드 호제법을 사용해주면 될 것 같다. 대신 1로 이루어진 수라는 조건을 이용하자
#A,B 입력받기
A,B = map(int,input().split())
if A<B:
        A,B = B,A
#1의 개수 a,b가 주어졌을 때 최대공약수를 구해주는 함수
while True:
     if A%B == 0:
          break
     A = A%B
     B,A = A,B

print(B*'1')