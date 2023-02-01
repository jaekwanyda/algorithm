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

def solution(files):
    answer = [];result=[['','',''] for i in range(len(files))]
    num_list=['0','1','2','3','4','5','6','7','8','9']
    for i,file in enumerate(files):
        cnt=0
        while not file[cnt] in num_list:
            cnt+=1
        result[i][0]=file[:cnt]
        cnt_i=cnt
        while file[cnt_i] in num_list:
            cnt_i+=1
            if cnt_i==len(file):
                break
        result[i][1]=file[cnt:cnt_i]
        if cnt_i<len(file):
            result[i][2]=file[cnt_i:]
    result=sorted(result,key=lambda x:(str.upper(x[0]),int(x[1])))
    for r in result:
        answer.append(''.join(r))
    return answer
