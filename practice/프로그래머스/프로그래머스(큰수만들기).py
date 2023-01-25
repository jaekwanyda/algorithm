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

def solution(number, k):
    answer = []
    for num in number:
        if len(answer)==0:
            answer.append(num)
            continue
        if k>0:
            while answer[-1]<num:
                answer.pop()
                k-=1
                if k<=0 or len(answer)==0:
                    break
        answer.append(num)
    answer=answer[:-k] if k>0 else answer
    return ''.join(answer)
