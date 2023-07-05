import sys
input = sys.stdin.readline
#아이디어:DP로 해결해보자
#N입력받기
n = int(input())
dp = [0]*(max(n,5)+1)
dp[1]=0;dp[2]=1;dp[3]=0;dp[4]=1;dp[5]=1
if n>5:
    for i in range(6,n+1):
          #1,3,4 전에 다 상근이가 이기면 이번엔 진다
          if dp[i-1] and dp[i-3] and dp[i-4]:
               dp[i] = 0
          else:
               dp[i] = 1
if dp[n]:
     print('SK')
else:
     print('CY')
