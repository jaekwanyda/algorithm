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

def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))];stack=[]
    for idx,i in enumerate(prices):
        cnt=0;length=len(stack)
        while length:
            idx1=stack[cnt][0];i1=stack[cnt][1]
            if i<i1:
                answer[idx1]=idx-idx1
                stack.pop(cnt)
            else:
                cnt+=1
            length-=1
        stack.append((idx,i))
    return answer
