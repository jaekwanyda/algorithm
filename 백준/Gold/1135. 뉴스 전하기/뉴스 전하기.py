import sys
input = sys.stdin.readline
#아이디어: 더 많은 시간이 걸리는 자식 먼저 전화하기
#n입력받기
n = int(input())
#상사 번호 입력받기
sup = list(map(int,input().split()))
#tree 만들어주기
tree = [[] for _ in range(n)]
for down, up in enumerate(sup):
    #부하 명단 만들기
    if up != -1:
        tree[up].append(down)
#부하에게 전화하는데 걸리는 시간을 저장
time = [0]*n
def dfs(up):
    #부하들이 걸리는 시간들 저장하기
    down_time = []
    for down in tree[up]:
        dfs(down) #부하의 부하들도 확인
        down_time.append(time[down])
    #부하들이 있다면 그 중 가장 시간이 오래 걸리는 놈-> 그 다음놈->... 순으로 간다
    if tree[up]:
        down_time.sort(reverse=True)
        down_time = [down_time[i]+i+1 for i in range(len(down_time))]
        #그 중 가장 시간이 오래걸린 것을 자신의 시간으로 등록한다.
        time[up] = max(down_time)
dfs(0)
print(time[0])
