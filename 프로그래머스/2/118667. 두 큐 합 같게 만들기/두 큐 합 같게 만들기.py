from collections import deque #약간의 시간 초과
def solution(queue1, queue2): 
    answer = 0
    total=sum(queue1)+sum(queue2)
    q1=deque(queue1);q2=deque(queue2)
    a=sum(q1)
    cnt=0
    while cnt<600001:
        if a>total/2:
            b=q1.popleft()
            q2.append(b)
            a-=b
            answer+=1
        elif a<total/2:
            b=q2.popleft()
            q1.append(b)
            a+=b
            answer+=1
        else:
            break
        if len(q1)==0 or len(q2)==0 or cnt==600000:
            answer=-1
            break
        cnt+=1
    return answer