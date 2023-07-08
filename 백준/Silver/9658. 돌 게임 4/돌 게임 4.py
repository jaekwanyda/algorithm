import sys
input = sys.stdin.readline
#아이디어:규칙 발견해보림
#N입력받기
n = int(input())
k = n%7
if k==1 or k==3:
    print('CY')
else:
    print('SK')
