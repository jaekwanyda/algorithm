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

def solution(citations):
    citations.sort()
    for i in range(citations[-1]+1):
        cnt=0
        for c in citations:
            if c>=i:
                cnt+=1
        if cnt>=i:
            answer=i
    return answer
