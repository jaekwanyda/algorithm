import sys
input = sys.stdin.readline
#아이디어: 그냥 구현하면 시간초과가 나기 때문에 각 줄별로 부분합을 저장해두자
#r,c,q입력받기
r,c,q = map(int,input().split())
#array 입력받기
array = [list(map(int,input().split())) for _ in range(r)]
#부분합 행렬만들기
array_sum = [[0]*c for _ in range(r)]
for i in range(r):
     for j in range(c):
          #첫번째는 그대로
          if i==0 and j == 0:
               array_sum[i][j] = array[i][j]
          elif i==0:
               array_sum[i][j] = array[i][j] + array_sum[i][j-1]
          elif j==0:
               array_sum[i][j] = array[i][j] + array_sum[i-1][j]
          else:
               array_sum[i][j] = array[i][j] + array_sum[i-1][j] +array_sum[i][j-1] - array_sum[i-1][j-1]        
for _ in range(q):
     #원하는 위치 입력받기
     r1,c1,r2,c2 = map(int,input().split())
     #총 합 저장하기
     if r1-1 == 0 and c1-1 == 0:
          s = array_sum[r2-1][c2-1]
     elif r1-1 == 0:
          s = array_sum[r2-1][c2-1] - array_sum[r2-1][c1-2]
     elif c1-1 == 0:
          s = array_sum[r2-1][c2-1] - array_sum[r1-2][c2-1]
     else:
          s = array_sum[r2-1][c2-1] - array_sum[r2-1][c1-2] - array_sum[r1-2][c2-1] + array_sum[r1-2][c1-2]
     print(s//((r2-r1+1)*(c2-c1+1)))