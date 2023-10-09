import sys
input = sys.stdin.readline
#아이디어: 계속해서 가능한 가장 작은 수를 입력한다. 만약 아예 안된다면 앞으로 돌아와 수를 바꾼다.
#n 입력받기
n = int(input())
#좋은 수열인지 확인해주는 함수
def good(s): #문자열 입력
    tmp = 2
    while tmp <= len(s)//2:
        if s[len(s)-tmp:] == s[len(s)-2*tmp:len(s)-tmp]:
            return False
        else:
            tmp += 1
    return True
stack = []
stack.append([1])
while stack:
    s = stack.pop()
    if len(s) == n:
        print(''.join((str(x) for x in s)))
        break
    for i in range(3,0,-1):
        if i != s[-1] and good(s+[i]):
            stack.append((s+[i]))
            