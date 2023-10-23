import sys
input = sys.stdin.readline
#아이디어: 팰린드롬이 아예 불가능한 경우는 모든 문자가 같은 경우밖에 없다.
char = input().rstrip()
if len(set(char)) == 1:
    print(-1)
else:
    if char == char[::-1]:
        print(len(char)-1)
    else:
        print(len(char))