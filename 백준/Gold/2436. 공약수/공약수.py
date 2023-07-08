import sys
input = sys.stdin.readline
#아이디어: 최대공약수로 최소공배수를 나눈다. 그럼 그 수의 약수를 이용할 수 잇다.
import math
#최대공약수, 최소공배수 입력받기
a,b = map(int,input().split())
c = b//a #이 수를 이루는 약수 중 가장 차이가 작고 서로가 서로소인 2수를 구해준다
#약수 찾기!
mn = int(math.sqrt(c)) #루트한 값을 기준으로 계속 1씩 줄여주자
while mn>0:
    #약수일 경우
    if c%mn == 0:
        mx = c//mn
        #서로소인 경우 print
        if math.gcd(mn,mx) ==1:
            print(mn*a,mx*a)
            break
    mn -=1
if mn == 0:
    print(a,b)