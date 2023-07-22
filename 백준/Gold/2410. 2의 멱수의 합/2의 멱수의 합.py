import sys
input = sys.stdin.readline
#아이디어: 홀수의 경우 전번의 +1 을 하면 되지만 짝수의 경우 2,4 ...2^k로 시작하는 경우도 생각해줘야 한다.
#n,m 입력받기
n = int(input())
#dp 만들기
dp = [0]*(max(n,3)+1)
dp[1] = 1;dp[2] = 2
for i in range(3,max(n,3)+1):
    #홀수는 그냥 전번
    if i%2 == 1:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i//2])%1000000000
print(dp[n])