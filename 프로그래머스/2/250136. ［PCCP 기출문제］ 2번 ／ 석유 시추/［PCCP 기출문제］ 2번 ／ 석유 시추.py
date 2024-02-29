def solution(land):
    from collections import deque
    visited = set()
    n = len(land)
    m = len(land[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    answer = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] and (i,j) not in visited:
                cnt = 0
                q = deque()
                q.append((i,j))
                visited.add((i,j))
                rows = set()
                rows.add(j)
                while q:
                    x,y = q.popleft()
                    cnt += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<= nx < n and 0<= ny < m and land[nx][ny] and not (nx,ny) in visited:
                            visited.add((nx,ny))
                            rows.add(ny)
                            q.append((nx,ny))
                for row in rows:
                    answer[row] += cnt
    
    return max(answer)