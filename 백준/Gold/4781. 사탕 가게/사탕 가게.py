import sys
input = sys.stdin.readline
#아이디어: 단순하게 칼로리당 가장 가격이 저렴한 사탕을 많이 사면 될 것 같다.(X)
#돈이 남는 경우는 그게 최선이 아닐 수 있다. => DP로 해결하기
#먼저 가장 최선의 캔디로 채운 후 다음 최선의 캔디가 있는 경우로 DP 를 만들어보자
while True:
    #n,m 입력 받기
    n,m = map(float,input().split())
    n,m = int(n),int(m*100+0.5)
    if n == 0 and m==0:
        break   
    #사탕 정보들 입력받기
    candies = []
    for _ in range(n):
        c,p  = map(float,input().split())
        c,p = int(c),int(p*100+0.5)
        candies.append([c,p])
    dp = [0]*(m+1)
    for i in range(n):
        cal,price = candies[i][0], candies[i][1]
        for j in range(m+1):
            if price <= j: #해당 사탕이 있는 경우, 없는 경우 중 큰 값으로 채워준다.
                dp[j] = max(dp[j], dp[j-price] + cal)
    print(dp[m])
        