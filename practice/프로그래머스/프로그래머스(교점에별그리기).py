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

# +
def meet(line1,line2):
    x=0.1;y=0.1
    if line1[0]*line2[1]-line1[1]*line2[0]!=0:
        x=(line1[1]*line2[2]-line1[2]*line2[1])/(line1[0]*line2[1]-line1[1]*line2[0])
    if line1[1]*line2[0]-line1[0]*line2[1]!=0:
        y=(line1[0]*line2[2]-line1[2]*line2[0])/(line1[1]*line2[0]-line1[0]*line2[1])
    return x,y

def solution(line):
    answer = []
    stars=set()
    result=[]
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            x,y=meet(line[i],line[j])
            if x%1==0 and y%1==0:
                stars.add((x,y))
    for i in stars:
        result.append(list(i))
    result.sort()
    column=result[-1][0]-result[0][0]+1
    left=result[0][0]
    result=sorted(result,key=lambda x:x[1])
    row=result[-1][1]-result[0][1]+1
    up=result[-1][1]
    for i in result:
        i[0]-=left;i[1]=abs(i[1]-up)
    print(result)
    for i in range(int(row)):
        a=''
        for j in range(int(column)):
            if [j,i] in result:
                a+='*'
            else:
                a+='.'
            if j==int(column)-1:
                answer.append(a)
    return answer
