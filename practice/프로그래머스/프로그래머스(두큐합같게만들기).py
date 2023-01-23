# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from collections import deque #약간의 시간 초과
def solution(queue1, queue2): 
    answer = 0
    total=sum(queue1)+sum(queue2)
    q1=deque();q2=deque()
    for i in queue1:
        q1.append(i)
    for i in queue2:
        q2.append(i)
    a=sum(q1)
    while True:
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
        if len(q1)==0 or len(q2)==0:
            answer=-1
            break
    return answer


from collections import deque 
#위의 코드에서 무한 루프에 갇힐 경우를 추가했음. 총 queue의 길이가 30만이 최대이므로 60만번 돌아도 해결이 안되면 -1출력
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
