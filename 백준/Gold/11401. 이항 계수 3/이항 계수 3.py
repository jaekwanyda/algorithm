import sys
input = sys.stdin.readline
#아이디어: 굉장히 복잡하게 해결 가능하다
#n,k 입력받기
n,k = map(int,input().split())
#nPk 부터
front = 1
for i in range(n,n-k,-1):
    front = (front*i) % 1000000007 
target = format(1000000005,'b')
start = 1
for i in range(1,k+1):
    start = (start*i) % 1000000007
target_list = []
cnt = 0
while cnt<len(target):
    target_list.append(start)
    start = (start*start) % 1000000007
    cnt += 1
back = 1
for i in range(len(target)):
    if int(target[i]):
        back *= (int(target[i])*target_list[-i-1]) % 1000000007
print(front*back% 1000000007)