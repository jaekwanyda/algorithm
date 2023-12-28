import sys
input = sys.stdin.readline
#아이디어: dp
n = int(input())
dp = [0]*(n+1)
pre_list = [0]*(n+1)
if n>=2:
    dp[2] = 1
    pre_list[2] = 1
if n>=3:
    dp[3] = 1
    pre_list[3] = 1
for i in range(4,max(4,n+1)):
    poss = [(dp[i-1]+1,i-1)]
    if i%2 == 0:
        poss.append((dp[i//2]+1,i//2))
    if i%3 == 0:
        poss.append((dp[i//3]+1,i//3))
    val,idx = min(poss,key=lambda x:x[0])
    dp[i],pre_list[i] = val,idx
print(dp[n])
result = [n]
start = n
while start != 1:
    start = pre_list[start]
    result.append(start)
print(*result) 