def solution(park, routes):
    answer = []
    direction_dict = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    for idx,p in enumerate(park):
        if p.find('S') != -1:
            x = idx
            y = p.find('S')
            break
    n = len(park)
    m = len(park[0])
    for route in routes:
        direction = direction_dict[route[0]]
        cnt = int(route[2:])
        nx = x
        ny = y
        possi = True
        for _ in range(cnt):
            nx += direction[0]
            ny += direction[1]
            if not(0<=nx<n and 0<=ny<m and park[nx][ny] != 'X'):
                possi = False
        if possi:
            x = nx
            y = ny
    return [x,y]