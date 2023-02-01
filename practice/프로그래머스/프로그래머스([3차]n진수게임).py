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

def make_n(n,cnt):
    array=[];dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    if cnt%n>=10:
        array.append(dic[cnt%n])
    else:
        array.append(str(cnt%n))
    while cnt>=n:
        cnt=cnt//n
        if cnt%n>=10:
            array.append(dic[cnt%n])
        else:
            array.append(str(cnt%n))
    array.reverse()
    return ''.join(array)
def solution(n, t, m, p):
    answer = '';result=''
    length=t*m;cnt=0
    while len(result)<length:
        result+=make_n(n,cnt)
        cnt+=1
    for i in range(t):
        answer+=result[i*m+p-1]
    return answer
