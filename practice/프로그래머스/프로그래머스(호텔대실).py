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
def end_time(end):#청소까지 처리한 퇴실 시간
    end=list(end)
    a=end[3]
    if int(a)<5:
        end[3]=str(int(end[3])+1)
    else:
        end[3]='0'
        b=end[1]
        if int(b)<9:
            end[1]=str(int(end[1])+1)
        else:
            end[1]='0'
            end[0]=str(int(end[0])+1)
    return ''.join(end)

def solution(book_time):
    answer = 0
    array=sorted(book_time,key=lambda x:(x[0],x[1]))
    while array:
        start,end=array.pop(0);cnt=0
        while cnt<len(array):
            if array[cnt][0]>=end_time(end):
                start,end=array.pop(cnt)
            else:
                cnt+=1
        answer+=1     
    return answer
