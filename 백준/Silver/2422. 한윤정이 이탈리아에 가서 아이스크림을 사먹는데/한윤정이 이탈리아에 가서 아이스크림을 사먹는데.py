import sys
input = sys.stdin.readline
#아이디어: 앞에서 부터 가능한 경우 세기, 뒤로 넘어가면 앞의 경우 생각 안하기
#n,m 입력받기
n,m = map(int,input().split())
graph=[[1 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 0
    graph[b][a] = 0
answer = 0    
for i in range(1,n-1):
    for j in range(i+1,n):
        if graph[i][j]:
            for k in range(j+1,n+1):
                if graph[i][k] and graph[j][k]:
                    answer += 1
print(answer)
