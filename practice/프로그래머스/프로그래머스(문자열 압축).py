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

def solution(s):
    answer = 987654321
    for i in range(1,len(s)+1):
        length=len(s);cnt=0
        for j in range(len(s)//i):
            if s[j*i:(j+1)*i]==s[(j+1)*i:(j+2)*i] :
                length-=i
                cnt+=1
            else:
                if cnt>=1:
                    length+=1
                    if cnt>=9:
                        length+=1
                        if cnt>=99:
                            length+=1
                            if cnt>=999:
                                length+=1
                    cnt=0
        if cnt>=1:
            length+=1
            if cnt>=9:
                length+=1
                if cnt>=99:
                    length+=1
                    if cnt>=999:
                        length+=1
        print(length,i)
        answer=min(length,answer)
            
    return answer
