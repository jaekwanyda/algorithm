def solution(n, m, x, y, r, c, k):
    path = ''
    vertical_moves = abs(r - x)
    horizontal_moves = abs(c - y) 

    if vertical_moves + horizontal_moves > k or (k - vertical_moves - horizontal_moves) % 2 != 0:
        return "impossible"
    
    stack = []

    remaining_vertical = (k-(vertical_moves+horizontal_moves))//2
    if r > x:
        remaining_vertical = min(remaining_vertical, n-x-vertical_moves)
        path += 'd' * (vertical_moves + remaining_vertical)
        stack += ['u'] * remaining_vertical
    else:
        remaining_vertical = min(remaining_vertical, n-x)
        path += 'd' * remaining_vertical
        stack += ['u'] * (vertical_moves + remaining_vertical)
    
    remaining_horizon = (k-len(path)-len(stack)-horizontal_moves)//2
    if c < y:
        remaining_horizon = min(remaining_horizon, y-horizontal_moves-1)
        path += 'l' * (horizontal_moves + remaining_horizon)
        stack += ['r'] * remaining_horizon
    else:
        remaining_horizon = min(remaining_horizon, y-1)
        path += 'l' * remaining_horizon
        stack += ['r'] * (horizontal_moves + remaining_horizon)
    
    remaining_moves = k - len(path) - len(stack)
    
    lr_sequence = 'rl' * (remaining_moves // 2)
    path += lr_sequence + ''.join(stack[::-1])

    return path