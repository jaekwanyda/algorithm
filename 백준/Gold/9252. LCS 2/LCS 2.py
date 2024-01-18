import sys
input = sys.stdin.readline
from collections import defaultdict
#아이디어: 2차원 dp (참고:https://soojong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9E%90%EB%B0%94-%EB%B0%B1%EC%A4%80-9252%EB%B2%88-LCS-2)
a_string = input().rstrip()
b_string = input().rstrip()
a = len(a_string)
b = len(b_string)
dp = [[0]*(a+1) for _ in range(b+1)]
for i in range(1,b+1):
    for j in range(1,a+1):
        if a_string[j-1] == b_string[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
answer = []
startx, starty = b,a
value = dp[startx][starty]
while startx  and starty:
    if dp[startx-1][starty] == value:
        startx -= 1
    elif dp[startx][starty-1] == value:
        starty -= 1
    elif dp[startx-1][starty-1] == value-1:
        answer.append(a_string[starty-1])
        startx -= 1
        starty -= 1
        value -= 1
    else:
        break
print(dp[b][a])
if dp[b][a]:
    print(''.join(answer[::-1]))