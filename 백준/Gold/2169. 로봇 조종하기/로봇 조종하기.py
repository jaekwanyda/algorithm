import sys
input = sys.stdin.readline
#아이디어: DP를 이용해서 오는 것 중 가장 큰 것을 계속 저장한다.
# N, M 입력받기
n,m = map(int,input().split())
# array 입력받기
array = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
#첫번째 줄은 왼쪽에서 오는 경우 밖에 없기 때문에 그냥 업데이트
dp[0][0] = array[0][0]
for i in range(1,m):
    dp[0][i] = dp[0][i-1] + array[0][i]
#두번째 줄부터는 위에서 오는 것 중, 왼쪽에서 오는 것 중, 오른쪽에서 오는 것 중 가장 큰 것 저장
for i in range(1,n):
    #위에서 오는 것
    up = dp[i-1][:]
    #왼쪽에서 오는 것
    left = array[i][:];left[0] = left[0] + up[0]
    for j in range(1,m):
        #왼쪽에서 오는 것과 위에서 오는 것 중 큰 값 고르기
        left[j] = max(left[j] + up[j] ,left[j] + left[j-1])
    #오른쪽에서 오는 것\
    right = array[i][:]; right[m-1] = right[m-1] + up[m-1]
    for j in range(m-2,-1,-1):
        #오른쪽에서 오는 것과 위에서 오는 것 중 큰 값 고르기
        right[j] = max(right[j] + up[j], right[j] + right[j+1])
    #그 중 가장 큰 것 dp에 등록
    for j in range(m):
        dp[i][j] = max(left[j],right[j])
print(dp[n-1][m-1])