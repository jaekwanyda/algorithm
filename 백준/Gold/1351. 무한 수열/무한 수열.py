import sys
input = sys.stdin.readline
#아이디어: dict와 재귀를 이용해서 이미 본 것들은 또 안보도록 해주자
n,p,q = map(int,input().split())
dp = {}
dp[0] = 1
def r(a):
    if a in dp:
        return dp[a]
    dp[a] = r(a//p) + r(a//q)
    return dp[a]
print(r(n))