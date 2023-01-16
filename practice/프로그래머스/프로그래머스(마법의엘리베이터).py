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

def solution(storey):
    answer = 0
    while storey:
        end_num=storey%10
        if end_num<5:
            answer+=end_num
            storey-=end_num
        elif end_num==5:
            if storey//10==0:
                answer+=end_num
                storey-=end_num
            else:
                b=storey//10
                next_end=b%10
                if next_end<=4:
                    answer+=end_num
                    storey-=end_num
                else:
                    answer+=10-end_num
                    storey+=10-end_num
                    
        else:
            answer+=10-end_num
            storey+=10-end_num
        storey=storey//10
    return answer
