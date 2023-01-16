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

def dfs_emo(users,emoticons,sales,max_list):
    if len(emoticons)==len(sales):
        plus_sum=0;sale_sum=0
        for i,j in users:
            q=0
            for k in range(len(sales)):
                if sales[k]*100>=i:
                    q+=emoticons[k]*(1-sales[k])
            if q>=j:
                plus_sum+=1
            
            else:
                sale_sum+=q
        if plus_sum>max_list[0]:
            max_list[0]=plus_sum
            max_list[1]=sale_sum
        elif plus_sum==max_list[0]:
            if sale_sum>=max_list[1]:
                max_list[0]=plus_sum
                max_list[1]=sale_sum
        sales=[]
        return max_list
    
    for i in range(1,5):
        a=sales+[i*0.1]
        dfs_emo(users,emoticons,a,max_list)
def solution(users, emoticons):
    sales=[]
    max_list=[0,0]
    dfs_emo(users,emoticons,sales,max_list)
    return max_list


