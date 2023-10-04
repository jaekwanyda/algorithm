import sys
input = sys.stdin.readline
#아이디어: 이용가능한 버튼으로 만드는 모든 경우 중 가장 가까운 부분을 찾아주자
from collections import deque
#채널번호 n 입력받기
n = int(input())
#고장난 버튼 수 입력받기
nums = int(input())
#고장난 버튼 정보 입력받기
botton = [1]*10
broke = list(map(int,input().split()))
for i in broke:
    botton[i] = 0
q = deque()
uses = []
answer = abs(n-100)
for i,b in enumerate(botton):
    if b:
        q.append((i,1)) #누른 버튼과 자리수
        answer = min(abs(n-i)+1,answer)
        uses += [i]
while q:
    b,d = q.popleft()
    for u in uses:
        if abs(10*b+u-n)+d+1 < abs(b-n)+d and 10*b+u-n < 10**7: #기존보다 작아지는 경우만 deque에 추가
            answer = min(abs(10*b+u-n)+d+1,answer)
            q.append((10*b+u, d+1))
print(answer)