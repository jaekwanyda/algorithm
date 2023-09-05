import sys
input = sys.stdin.readline
#아이디어: 순회가 중위 순회(inoder) 방식이다. 이것을 이용해보자
from collections import deque
#k 입력받기
k = int(input())
#방문한 번호 입력받기
array = list(map(int,input().split()))
#중앙의 번호 출력 후 양쪽의 중앙 출력(반복)
q = deque()
#처음 중앙값
q.append(len(array)//2)
n = len(array)//2 + 1
while n:
    #같은 높이 전부 출력
    p = deque() #출력된 것들 저장하는 deque
    n = n//2
    while q:
        a = q.popleft()
        p.append(a)
        print(array[a],end=' ')
    while p:
        b = p.popleft()
        q.append(b-n)
        q.append(b+n)    
    print('')