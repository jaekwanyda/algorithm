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

from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_list=[0]*len(skill)
        q=deque();skill_posi=True
        for j in i:
            if j in skill:
                q.append(j)
        print(q)
        while q:
            x=q.popleft()
            a=skill.find(x)
            skill_list[a]=1
            for i in range(a,-1,-1):
                if skill_list[i]==0:
                    skill_posi=False
        if skill_posi:
                answer+=1
    return answer
