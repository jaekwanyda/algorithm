def solution(n, t, m, timetable):
    from collections import deque
    q = deque(sorted(int(t[:2])*60 + int(t[3:]) for t in timetable))
    answer = -1
    time = 9*60
    for i in range(n):
        tmp = m
        while q and tmp:
            c = q.popleft()
            if c <= time:
                tmp -= 1
                final = c
            else:
                q.appendleft(c)
                break
        if tmp:
            answer = time
        time += t
    if not tmp:
        answer = final-1
    hour = str(answer//60)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(answer%60)
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ':' + minute