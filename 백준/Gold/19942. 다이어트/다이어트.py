import sys
input = sys.stdin.readline

# n 입력받기
n = int(input())
# 최소 영양성분 입력받기
mp, mf, ms, mv = map(int, input().split())
# 영양성분들 입력받기
g_list = []
for _ in range(n):
    g_list.append(list(map(int, input().split())))

min_cost = 9999999
answer = []

def dfs(m, g, total_cost, total_list):
    global answer, min_cost

    if m == n:
        if total_cost < min_cost and g[0] >= mp and g[1] >= mf and g[2] >= ms and g[3] >= mv:
            answer = total_list[:]
            min_cost = total_cost
    else:
        for i in range(2):
            if i==0:
                # 더해주는 경우
                b = total_list[:]
                b.append(1)
                g_new = [g[i] + g_list[m][i] for i in range(4)]
                total_cost_new = total_cost + g_list[m][4] 
                if total_cost_new < min_cost and g_new[0] >= mp and g_new[1] >= mf and g_new[2] >= ms and g_new[3] >= mv:
                    answer = b[:]
                    min_cost = total_cost_new
                dfs(m + 1, g_new, total_cost_new, b)
            else:
                # 안더해주는 경우
                a = total_list[:]
                a.append(0)
                dfs(m+1, g, total_cost, a)

dfs(0, [0, 0, 0, 0], 0, [])
answer_idx = []
for idx,i in enumerate(answer):
    if i==1:
        answer_idx.append(idx+1)
if min_cost==9999999:
    print(-1)
else:
    print(min_cost)
    print(*answer_idx)